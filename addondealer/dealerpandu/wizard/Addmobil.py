from odoo import api, fields, models


class Addmobil(models.Model):
    _name = 'dealerpandu.addmobil'

    daftarmobil_id = fields.Many2one(comodel_name='dealerpandu.daftarmobil', string='Daftar Mobil')
    jumlah = fields.Integer(string='Jumlah')

    def button_add_mobil(self):
        for rec in self:
            self.env['dealerpandu.daftarmobil']\
                .search([('id','=',rec.daftarmobil_id.id)])\
                .write({'stock': rec.daftarmobil_id.stock + rec.jumlah})
    
    
