# -*- coding: utf-8 -*-
# from odoo import http


# class ProductBox(http.Controller):
#     @http.route('/product_box/product_box/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_box/product_box/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_box.listing', {
#             'root': '/product_box/product_box',
#             'objects': http.request.env['product_box.product_box'].search([]),
#         })

#     @http.route('/product_box/product_box/objects/<model("product_box.product_box"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_box.object', {
#             'object': obj
#         })
