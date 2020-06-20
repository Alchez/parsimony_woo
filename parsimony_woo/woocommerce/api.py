
from woocommerce import API

import frappe


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
