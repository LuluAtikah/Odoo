# -*- coding: utf-8 -*-
from openerp import http

# class Mutabaah(http.Controller):
#     @http.route('/mutabaah/mutabaah/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mutabaah/mutabaah/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mutabaah.listing', {
#             'root': '/mutabaah/mutabaah',
#             'objects': http.request.env['mutabaah.mutabaah'].search([]),
#         })

#     @http.route('/mutabaah/mutabaah/objects/<model("mutabaah.mutabaah"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mutabaah.object', {
#             'object': obj
#         })