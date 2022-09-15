from asyncore import file_dispatcher
from odoo import api, fields, models


class InvoiceOrder(models.TransientModel):
    _name = 'dealerpandu.wizardinvoiceorder'

    konsumen_id = fields.Many2one(comodel_name='res.partner', string='Konsumen')
    dari_tgl = fields.Date(string='Dari Tanggal')
    ke_tgl = fields.Date(string='Ke Tanggal')
    
    #MASIH EROR
    def button_wizard_invoice_order_action(self):
        filter =[]
        konsumen_id = self.konsumen_id
        dari_tgl = self.dari_tgl
        ke_tgl = self.ke_tgl
        if konsumen_id:
            filter += [('nama_pembeli', '=', konsumen_id.id)]
        if dari_tgl:
            filter += [('tgl_order', '>=', dari_tgl)]
        if ke_tgl:
            filter += [('tgl_order', '<=', ke_tgl)]
        print(filter)
        order = self.env['dealerpandu.order'].search_read(filter)
        print(order)
        data = {
            'form': self.read()[0],
            'orderxx': order
        }
        return self.env.ref('dealerpandu.wizard_invoice_order_pdf').report_action(self, data=data)
