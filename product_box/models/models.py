# -*- coding: utf-8 -*-

from odoo import models, fields, api


class product_box(models.Model):
    _inherit = 'product.template'


    sqft_pro = fields.Float("SqFt")
    tiles_value = fields.Float("Tiles Qty")


class product_box(models.Model):
    _inherit = 'sale.order.line'

    sqft_pro = fields.Float("SqFt")
    tiles_value = fields.Float("Tiles Qty")

    @api.onchange('product_uom_qty','product_id')
    def _onchange_parent_id(self):

       for i in self:
           i.sqft_pro=i.product_id.sqft_pro*i.product_uom_qty
           i.tiles_value = i.product_id.tiles_value*i.product_uom_qty











