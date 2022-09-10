from odoo import models, fields, api


class Fleet(models.Model):
    _inherit = 'fleet.vehicle'
    _description = 'New Description'

    is_sport = fields.Boolean(string='Mobil Sport')
    is_suv = fields.Boolean(string='Mobil SUV')
    
    