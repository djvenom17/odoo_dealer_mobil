from odoo import models, fields, api


class ModuleName(models.Model):
    _inherit = 'res.partner'

    plat_mobil = fields.Char(string='Plat Mobil')
    employee_junior = fields.Boolean('Junior')
    employee_senior = fields.Boolean('Senior')
