# -*- coding: utf-8 -*-
from odoo import http

# class MethodReportWarehouse(http.Controller):
#     @http.route('/method_report_warehouse/method_report_warehouse/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_report_warehouse/method_report_warehouse/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_report_warehouse.listing', {
#             'root': '/method_report_warehouse/method_report_warehouse',
#             'objects': http.request.env['method_report_warehouse.method_report_warehouse'].search([]),
#         })

#     @http.route('/method_report_warehouse/method_report_warehouse/objects/<model("method_report_warehouse.method_report_warehouse"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_report_warehouse.object', {
#             'object': obj
#         })