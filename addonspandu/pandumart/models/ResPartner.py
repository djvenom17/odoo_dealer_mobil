from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    is_konsumen = fields.Boolean(string='Konsumen')
    is_direksi = fields.Boolean(string='Direksi')
    id_member = fields.Char(string='ID Member', required=False, domain="[('is_konsumen','=', True)]")
    poin = fields.Integer(string='Poin')
    level = fields.Integer(string='Level')
    
    