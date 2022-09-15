from odoo import api, fields, models


class BrandMobil(models.Model):
    _name = 'dealerpandu.brandmobil'
    _description = 'New Description'

    name = fields.Selection(string='Nama Brand', selection=[('ferari', 'Ferari'),
                                                            ('lamborghini','Lamborghini'),
                                                            ('toyota', 'Toyota'),
                                                            ('honda','Honda')])
    founder_brand = fields.Char(string='Founder Brand')
    brand_country = fields.Char(string='Brand Country', onchange='_onchange_nama_brand')
    jml_mobil = fields.Char(compute='_compute_jml_mobil', string='Jumlah Mobil')
    logo_brand = fields.Image(string='Logo Brand Mobil')
    daftar = fields.Char(string='Daftar Mobil')
    daftarmobil_ids = fields.One2many(comodel_name='dealerpandu.daftarmobil', 
                                      inverse_name='brandmobil_id', 
                                      string='Daftar Mobil')
    
    #menu selection otomatis
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


    #jumlah mobil didalam sebuah brand
    @api.depends('daftarmobil_ids')
    def _compute_jml_mobil(self):
        for rec in self:
            a = self.env['dealerpandu.daftarmobil'].search([('brandmobil_id','=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_mobil = b
            rec.daftar = a
        
