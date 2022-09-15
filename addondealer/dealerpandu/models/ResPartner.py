from odoo import models, fields, api


class ModuleName(models.Model):
    _inherit = 'res.partner'

    plat_mobil = fields.Char(string='Plat Mobil')
    employee_junior = fields.Boolean('silver')
    employee_senior = fields.Boolean('gold')
    member_silver = fields.Boolean('Silver')
    member_gold = fields.Boolean('Gold')
