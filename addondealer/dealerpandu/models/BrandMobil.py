from odoo import api, fields, models


class BrandMobil(models.Model):
    _name = 'dealerpandu.brandmobil'
    _description = 'New Description'

    name = fields.Char(string='Nama Brand')
    brand_id = fields.Char(string='Kode Brand Mobil')
    

