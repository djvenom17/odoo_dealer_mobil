from odoo import models, fields


class Konsumen(models.Model):
    _inherit = 'res.partner'
    _description = 'konsumen'

    poin = fields.Integer(string='Poin')
    level = fields.Integer(string='Level')
    
    