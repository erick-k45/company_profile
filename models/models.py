# -*- coding: utf-8 -*-

from openerp import models, fields, api

class company_profile(models.Model):
    _name = 'company_profile.profile'

    name_c = fields.Char(string="Company Name")
    mission = fields.Text(string="Company Mission")
    view = fields.Text(string="Company View")
    values = fields.Text(string="Company Values")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
