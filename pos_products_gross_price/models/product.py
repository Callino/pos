# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, fields, models, api
import odoo.addons.decimal_precision as dp


class Product(models.Model):
    _inherit = 'product.product'

    @api.depends('lst_price', 'product_tmpl_id.taxes_id')
    def _compute_product_lst_price_gross(self):
        for product in self:
            taxes = product.taxes_id.compute_all(product.lst_price, quantity=1, product=product)
            product.lst_price_gross = taxes['total_included']

    lst_price_gross = fields.Float('Sale Price Gross', compute='_compute_product_lst_price_gross',
                                   digits=dp.get_precision('Product Price'))
