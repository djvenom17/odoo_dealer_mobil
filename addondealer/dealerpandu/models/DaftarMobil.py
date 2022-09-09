from odoo import api, fields, models


class DaftarMobil(models.Model):
    _name = 'dealerpandu.daftarmobil'
    _description = 'New Description'

    name = fields.Char(string='Nama Mobil')
    mobil_id = fields.Char(string='ID Mobil')
    harga_mobil = fields.Integer(string='Harga Mobil')
    
    
