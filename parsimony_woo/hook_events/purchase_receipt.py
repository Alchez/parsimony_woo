import frappe
from parsimony_woo.woocommerce.api import get_woocommerce_client


def update_stock_in_woocommerce(purchase_receipt, method):
	wc_client = get_woocommerce_client()

	if not wc_client:
		return

	for item in purchase_receipt.items:
		woocommerce_id = frappe.db.get_value("Item", item.item_code, "woocommerce_id")
		if not woocommerce_id:
			continue

		woocommerce_item = wc_client.get("products/{id}".format(id=woocommerce_id)).json()
		current_wc_stock = woocommerce_item.get("stock_quantity")

		new_wc_stock = current_wc_stock
		if method == "on_submit":
			new_wc_stock += item.qty
		elif method == "on_cancel":
			new_wc_stock -= item.qty

		if new_wc_stock != current_wc_stock:
			wc_client.put("products/{id}".format(id=woocommerce_id), {
				"stock_quantity": new_wc_stock
			})
