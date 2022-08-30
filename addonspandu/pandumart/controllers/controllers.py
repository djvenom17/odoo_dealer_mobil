# -*- coding: utf-8 -*-
# from odoo import http


# class Pandumart(http.Controller):
#     @http.route('/pandumart/pandumart', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pandumart/pandumart/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pandumart.listing', {
#             'root': '/pandumart/pandumart',
#             'objects': http.request.env['pandumart.pandumart'].search([]),
#         })

#     @http.route('/pandumart/pandumart/objects/<model("pandumart.pandumart"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pandumart.object', {
#             'object': obj
#         })
