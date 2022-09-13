from odoo import models, fields, api


class Employees(models.Model):
    _inherit = 'hr.employee'

    plat_mobil = fields.Char(string='Plat Mobil')
    employee_junior = fields.Boolean('Junior')
    employee_senior = fields.Boolean('Senior')

