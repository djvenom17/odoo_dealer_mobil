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
    


    #  name = fields.Char(string='Nama Barang')
    # harga_beli = fields.Integer(string='Harga Modal', required=True)
    # harga_jual = fields.Integer(string='Harga Jual', required=True)
    # kelompokbarang_id = fields.Many2one(comodel_name='pandumart.kelompokbarang', 
    #                                   string='Kelompok Barang',
    #                                   ondelete='cascade')
    # supplier_id = fields.Many2many(comodel_name='pandumart.supplier', string='Supplier')
    # stock = fields.Integer(string='Stock')
    
    # _sql_constraints = [
    #     ('nama_barang_unik','unique (name)','Nama Barang Sudah Terdaftar'),
    #     ('kelompokbarang_id_notnull','CHECK (kelompokbarang_id IS NOT NULL)','Kelompok Barang Gaboleh Kosong Dong !!!')
    #     ]
    
    # @api.constrains('stock')
    # def check_stock(self):
    #     for rec in self:
    #         if rec.stock < 1 :
    #             raise ValidationError('Isi Stock {} Terlebih dahulu '.format(rec.name))
    
