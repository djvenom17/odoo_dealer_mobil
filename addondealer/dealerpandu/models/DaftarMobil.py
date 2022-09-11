from odoo import api, fields, models


class DaftarMobil(models.Model):
    _name = 'dealerpandu.daftarmobil'
    _description = 'New Description'

    name = fields.Char(string='Nama Mobil')
    harga_mobil_modal = fields.Integer(string='Harga Modal Mobil', required=True)
    harga_mobil_jual = fields.Integer(string='Harga Jual Mobil', required=True)
    stock = fields.Integer(string='Stock Mobil')
    brandmobil_id = fields.Many2one(comodel_name='dealerpandu.brandmobil', 
                                    string='Brand Mobil',
                                    ondelete='cascade')
    dealermitra_id = fields.Many2many(comodel_name='dealerpandu.dealermitra', string='Deale Mitra')
    
    


    