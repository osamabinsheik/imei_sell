# -*- coding: utf-8 -*-
from odoo import http

# class ImeiSell(http.Controller):
#     @http.route('/imei_sell/imei_sell/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/imei_sell/imei_sell/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('imei_sell.listing', {
#             'root': '/imei_sell/imei_sell',
#             'objects': http.request.env['imei_sell.imei_sell'].search([]),
#         })

#     @http.route('/imei_sell/imei_sell/objects/<model("imei_sell.imei_sell"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('imei_sell.object', {
#             'object': obj
#         })