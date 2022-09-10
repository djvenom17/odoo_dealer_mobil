from odoo import api, fields, models


class BrandMobil(models.Model):
    _name = 'dealerpandu.brandmobil'
    _description = 'New Description'

    name = fields.Selection(string='Nama Brand', selection=[('ferari', 'Ferari'),
                                                            ('lamborghibi','Lamborghini'),
                                                            ('toyota', 'Toyota'),
                                                            ('honda','Honda')])
    founder_brand = fields.Char(string='Founder Brand')
    brand_country = fields.Char(string='Brand Country', onchange='_onchange_nama_brand')
    jml_mobil = fields.Char(compute='_compute_jml_mobil', string='Jumlah Mobil')
    logo_brand = fields.Image(string='Logo Brand Mobil')
    daftar = fields.Char(string='Daftar Isi')
    daftarmobil_ids = fields.One2many(comodel_name='dealerpandu.daftarmobil', 
                                      inverse_name='brandmobil_id', 
                                      string='Daftar Mobil')
    
    
    @api.onchange('name')
    def _onchange_nama_brand(self):
        if (self.name == 'ferari'):
            self.brand_country = 'italy'
        elif (self.name == 'lamborghini'):
            self.brand_country = 'italy'
        elif (self.name == 'toyota'):
            self.brand_country = 'japan'
        elif (self.name == 'honda'):
            self.brand_country = 'japan'

    @api.depends('daftarmobil_ids')
    def _compute_jml_mobil(self):
        for rec in self:
            a = self.env['dealerpandu.daftarmobil'].search([('brandmobil_id','=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_mobil = b
            rec.daftar = a
        

    # name = fields.Selection(string='Nama Kelompok', 
    #                         selection=[('makananbasah', 'Makanan Basah'), 
    #                                    ('makanankering', 'Makanan Kering'), 
    #                                    ('minuman','Minuman')])                                   
    # kode_kelompok = fields.Char(onchange='_compute_kode_kelompok', string='Kode Kelompok')
    # kode_rak = fields.Char(string='Kode Rak')
    # barang_ids = fields.One2many(comodel_name='pandumart.barang', 
    #                              inverse_name='kelompokbarang_id', 
    #                              string='Daftar Barang')
    # jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah Item')
    # daftar = fields.Char(string='Daftar Isi')
    
    # @api.onchange('name')
    # def _compute_kode_kelompok(self):
    #     if (self.name == 'makananbasah'):
    #         self.kode_kelompok = 'mak01'
    #     elif (self.name == 'makanankering'):
    #         self.kode_kelompok = 'mak02'
    #     elif (self.name == 'minuman'):
    #         self.kode_kelompok = 'min'
   
    # @api.depends('barang_ids')
    # def _compute_jml_item(self):
    #     for rec in self:
    #         a = self.env['pandumart.barang'].search([('kelompokbarang_id','=', rec.id)]).mapped('name')
    #         b = len(a)
    #         rec.jml_item = b
    #         rec.daftar = a

