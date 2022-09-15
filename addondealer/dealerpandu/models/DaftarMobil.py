from odoo import api, fields, models
from odoo.exceptions import ValidationError



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
    currency_id = fields.Many2one('res.currency', string='Account Currency',
        help="Forces all moves for this account to have this account currency.")
    
    _sql_constraints = [
        ('nama_mobil_unik','unique (name)','Nama Mobil Sudah Terdaftar'),
        ]
    
    @api.constrains('stock')
    def check_stock(self):
        for rec in self:
            if rec.stock < 1 :
                raise ValidationError('Isi Stock {} Terlebih dahulu '.format(rec.name))

    