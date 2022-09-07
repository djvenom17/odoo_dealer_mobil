from odoo import api, fields, models


class BarangDatang(models.TransientModel):
    _name = 'pandumart.barangdatang'


    barang_id = fields.Many2one(
                comodel_name='pandumart.barang', 
                string='Nama Barang',
                required=True)

    jumlah = fields.Integer(
                string='Jumlah',
                required=False)
    
    def button_barang_datang(self):
        for rec in self:
            self.env['pandumart.barang']\
                .search([('id','=',rec.barang_id.id)])\
                .write({'stock': rec.barang_id.stock + rec.jumlah})