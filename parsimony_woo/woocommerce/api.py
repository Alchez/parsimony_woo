import json

from woocommerce import API

import frappe
from erpnext.erpnext_integrations.connectors.woocommerce_connection import order, verify_request
from erpnext.selling.doctype.sales_order.sales_order import make_delivery_note, make_sales_invoice


def get_woocommerce_client():
	settings = frappe.get_single("Woocommerce Settings")

	if not settings.enable_sync:
		return

	return API(
		url=settings.woocommerce_server_url,
		consumer_key=settings.api_consumer_key,
		consumer_secret=settings.api_consumer_secret,
		wp_api=True,
		version="wc/v3",
		verify_ssl=False
	)


@frappe.whitelist(allow_guest=True)
def create_order(*args, **kwargs):
	# let ERPNext process the request and create an order
	order(*args, **kwargs)

	try:
		# auto-create an invoice for the new order
		_create_invoice(*args, **kwargs)
	except Exception:
		error_message = frappe.get_traceback() + "\n\n Request Data: \n" + json.loads(frappe.request.data).__str__()
		frappe.log_error(error_message, "WooCommerce Create Invoice Error")
		raise


@frappe.whitelist(allow_guest=True)
def update_order(*args, **kwargs):
	try:
		_update_order(*args, **kwargs)
	except Exception:
		error_message = frappe.get_traceback() + "\n\n Request Data: \n" + json.loads(frappe.request.data).__str__()
		frappe.log_error(error_message, "WooCommerce Update Order Error")
		raise


def _create_invoice(*args, **kwargs):
	order = frappe.get_last_doc("Sales Order")
	invoice = make_sales_invoice(order.name, ignore_permissions=True)
	invoice.save()
	invoice.submit()


def _update_order(*args, **kwargs):
	if frappe.request and frappe.request.data:
		verify_request()
		try:
			order = json.loads(frappe.request.data)
		except ValueError:
			# woocommerce returns 'webhook_id=value' for the first request which is not JSON
			order = frappe.request.data
		event = frappe.get_request_header("X-Wc-Webhook-Event")
	else:
		return "success"

	if event == "updated":
		sales_order = frappe.db.exists("Sales Order", {"woocommerce_id": order.get("id")})
		if not sales_order:
			return "success"

		# if a Woocommerce order is processing, then it has been shipped, but not fulfilled yet
		# ref: https://docs.woocommerce.com/document/managing-orders/#section-21
		if order.get("status") == "processing":
			existing_deliveries = frappe.get_all("Delivery Note Item",
				filters={"docstatus": 1, "against_sales_order": sales_order},
				fields=["parent"],
				distinct=True)

			if existing_deliveries:
				return "success"

			delivery_note = make_delivery_note(sales_order)
			delivery_note.save()
			delivery_note.submit()
