# -*- coding: utf-8 -*-

from odoo import models, fields, api


class product_box(models.Model):
    _inherit = 'product.template'


    sqft_pro = fields.Float("SqFt")
    tiles_value = fields.Float("Tiles Qty")


class product_box(models.Model):
    _inherit = 'sale.order.line'

    sqft_pro = fields.Float("SqFt",compute="_onchange_compute_sqft")
    tiles_value = fields.Float("Tiles Qty",compute="_onchange_compute_tiles")

    @api.depends('product_uom_qty','product_id')
    def _onchange_compute_tiles(self):

       for i in self:

           i.tiles_value = i.product_id.tiles_value * i.product_uom_qty



    @api.depends('product_uom_qty','product_id')
    def _onchange_compute_sqft(self):

       for i in self:
           i.sqft_pro = i.product_id.sqft_pro * i.product_uom_qty












