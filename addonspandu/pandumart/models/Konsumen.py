from odoo import models, fields


class Konsumen(models.Model):
    _inherit = 'res.partner'
    _description = 'konsumen'

    poin = fields.Integer(string='poin')
    level = fields.Char(string='level')
    
    