from asyncore import file_dispatcher
from odoo import api, fields, models


class PenjualanReport(models.TransientModel):
    _name = 'pandumart.penjualanreport'

    konsumen_id = fields.Many2one(comodel_name='res.partner', string='Konsumen')
    dari_tgl = fields.Date('Dari Tanggal')
    ke_tgl = fields.Date('Ke Tanggal')
    
    def button_penjualan_report_action(self):
        filter =[]
        konsumen_id = self.konsumen_id
        dari_tgl = self.dari_tgl
        ke_tgl = self.ke_tgl
        if konsumen_id:
            filter += [('nama_pembeli', '=', konsumen_id.id_member)]
        if dari_tgl:
            filter += [('tgl_penjualan','>=', dari_tgl)]
        if ke_tgl:
            filter += [('tgl_penjualan', '<=', ke_tgl)]
        penjualan = self.env['pandumart.penjualan'].search(filter)
        
        data = {
            'form': self.read()[0],
            'penjualan': penjualan
        }
        return self.env.ref('pandumart.wizard_penjualanreport_pdf').report_action(self, data=data)
        