# -*- coding: utf-8 -*-
# from odoo import http


# class Dealerpandu(http.Controller):
#     @http.route('/dealerpandu/dealerpandu', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dealerpandu/dealerpandu/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dealerpandu.listing', {
#             'root': '/dealerpandu/dealerpandu',
#             'objects': http.request.env['dealerpandu.dealerpandu'].search([]),
#         })

#     @http.route('/dealerpandu/dealerpandu/objects/<model("dealerpandu.dealerpandu"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dealerpandu.object', {
#             'object': obj
#         })
