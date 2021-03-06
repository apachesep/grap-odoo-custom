# Copyright (C) 2013-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "GRAP - Change Product Views",
    "version": "12.0.0.0.3",
    "category": "GRAP - Custom",
    "author": "GRAP",
    "website": "http://www.grap.coop",
    "license": "AGPL-3",
    "depends": [
        # Odoo Modules
        "product",
        "purchase",
        "sale",
        "point_of_sale",
        "stock",
        # Other Modules
        "fiscal_company_product",
        "product_margin_classification",
        "stock_preparation_category",
        "recurring_consignment",
        "product_margin_classification",
        "barcodes_generator_product",
        "product_to_scale_bizerba",
        "sale_eshop",
        "product_food",
        "product_label",
        "product_print_category",
        "product_print_category_food_report",
        "product_origin",
        "product_origin_l10n_fr_department",
        "product_form_purchase_link",
        "pos_meal_voucher",
        "product_notation",
        "purchase_package_qty",
        "purchase_discount",
        "purchase_triple_discount",
        "account_invoice_supplierinfo_update_standard_price",
        "product_standard_price_tax_included",
        "product_sale_tax_price_included",
        "pos_sector",
        # TODO
        # "grap_qweb_report",
    ],
    "data": [
        "views/menu.xml",
        "views/view_product_margin_classification.xml",
        "views/view_product_pricelist.xml",
        "views/view_product_pricelist_item.xml",
        "views/view_product_supplierinfo.xml",
        "views/view_product_product_tree.xml",
        "views/view_product_product_form.xml",
    ],
    "installable": True,
}
