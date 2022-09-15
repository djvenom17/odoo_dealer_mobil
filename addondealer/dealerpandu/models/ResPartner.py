from odoo import models, fields, api


class ModuleName(models.Model):
    _inherit = 'res.partner'

    member_silver = fields.Boolean('Silver')
    member_gold = fields.Boolean('Gold')

