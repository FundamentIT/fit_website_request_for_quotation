# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    website_request_quote = fields.Boolean(string="Request for Quotation",
        help="Allow user to send request for Quotation instade of directly add to cart")
