# -*- coding: utf-8 -*-
# from odoo import http


# class SimpleContact(http.Controller):
#     @http.route('/simple_contact/simple_contact', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/simple_contact/simple_contact/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('simple_contact.listing', {
#             'root': '/simple_contact/simple_contact',
#             'objects': http.request.env['simple_contact.simple_contact'].search([]),
#         })

#     @http.route('/simple_contact/simple_contact/objects/<model("simple_contact.simple_contact"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('simple_contact.object', {
#             'object': obj
#         })

