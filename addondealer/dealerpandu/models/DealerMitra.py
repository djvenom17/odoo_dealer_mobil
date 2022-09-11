from odoo import api, fields, models


class DealerMitra(models.Model):
    _name = 'dealerpandu.dealermitra'
    _description = 'New Description'

    name = fields.Char(string='Nama Dealer')
    alamat_dealer = fields.Char(string='Alamat Dealer')
    no_telp = fields.Char(string='No. Telp')
    logo_dealer = fields.Image(string='Logo Dealer')
    daftarmobil_id = fields.Many2many(comodel_name='dealerpandu.daftarmobil', string='Daftar Mobil')
    
    
    
