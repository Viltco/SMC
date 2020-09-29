# -*- coding: utf-8 -*-

from odoo import models, fields, api
class product_box(models.Model):
    _inherit = 'product.template'


    article_id = fields.Char(string='Article' )

    finish_id = fields.Char(string='Finish')



class product_box(models.Model):
    _inherit = 'stock.quant'

    qty_pro = fields.Float("Net Qty",compute="_onchange_compute_tiles")
    net_value = fields.Float("Net Value",compute="_onchange_compute_net_value")
    article_id = fields.Char(string='Article',
                             related='product_id.article_id')

    finish_id = fields.Char(string='Finish',
                            related='product_id.finish_id')

    def _onchange_compute_tiles(self):

        for i in self:

            i.qty_pro = i.quantity- i.reserved_quantity

    def _onchange_compute_net_value(self):

        for i in self:

            i.net_value = i.qty_pro *i.product_id.standard_price
















