# -*- coding: utf-8 -*-
# from odoo import http


# class Addons/recepcion(http.Controller):
#     @http.route('/addons/recepcion/addons/recepcion', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons/recepcion/addons/recepcion/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons/recepcion.listing', {
#             'root': '/addons/recepcion/addons/recepcion',
#             'objects': http.request.env['addons/recepcion.addons/recepcion'].search([]),
#         })

#     @http.route('/addons/recepcion/addons/recepcion/objects/<model("addons/recepcion.addons/recepcion"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons/recepcion.object', {
#             'object': obj
#         })
