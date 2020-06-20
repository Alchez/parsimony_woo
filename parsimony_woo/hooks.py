# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "parsimony_woo"
app_title = "Parsimony Woo"
app_publisher = "developers@parsimony.com"
app_description = "WooCommerce integration with Parsimony"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "developers@parsimony.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/parsimony_woo/css/parsimony_woo.css"
# app_include_js = "/assets/parsimony_woo/js/parsimony_woo.js"

# include js, css files in header of web template
# web_include_css = "/assets/parsimony_woo/css/parsimony_woo.css"
# web_include_js = "/assets/parsimony_woo/js/parsimony_woo.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "parsimony_woo.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "parsimony_woo.install.before_install"
# after_install = "parsimony_woo.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "parsimony_woo.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Delivery Note": {
		"on_submit": "parsimony_woo.hook_events.delivery_note.update_stock_in_woocommerce",
		"on_cancel": "parsimony_woo.hook_events.delivery_note.update_stock_in_woocommerce"
	},
	"Purchase Receipt": {
		"on_submit": "parsimony_woo.hook_events.purchase_receipt.update_stock_in_woocommerce",
		"on_cancel": "parsimony_woo.hook_events.purchase_receipt.update_stock_in_woocommerce"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"parsimony_woo.tasks.all"
# 	],
# 	"daily": [
# 		"parsimony_woo.tasks.daily"
# 	],
# 	"hourly": [
# 		"parsimony_woo.tasks.hourly"
# 	],
# 	"weekly": [
# 		"parsimony_woo.tasks.weekly"
# 	]
# 	"monthly": [
# 		"parsimony_woo.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "parsimony_woo.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "parsimony_woo.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "parsimony_woo.task.get_dashboard_data"
# }
