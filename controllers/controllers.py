# -*- coding: utf-8 -*-
from openerp import http

# class CompanyProfile(http.Controller):
#     @http.route('/company_profile/company_profile/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/company_profile/company_profile/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('company_profile.listing', {
#             'root': '/company_profile/company_profile',
#             'objects': http.request.env['company_profile.company_profile'].search([]),
#         })

#     @http.route('/company_profile/company_profile/objects/<model("company_profile.company_profile"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('company_profile.object', {
#             'object': obj
#         })