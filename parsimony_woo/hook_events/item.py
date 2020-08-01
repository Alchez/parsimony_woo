import frappe


def set_valuation_rate(item_doc, item_data):
	# process valuation rate for the item using a third-party plugin
	# https://wordpress.org/plugins/cost-of-goods-for-woocommerce/

	metadata = item_data.get("meta_data", [])
	for data in metadata:
		if data.get("key") == "_alg_wc_cog_item_cost":
			# TODO: change the valuation rate to a different default
			item_doc.valuation_rate = data.get("value", 0.01)

	return item_doc
