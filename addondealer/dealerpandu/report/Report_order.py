from odoo import api, fields, models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.dealerpandu.report_order_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, order):
        sheet = workbook.add_worksheet('Daftar Order History')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(2, 0, 'Order History')
        sheet.write(4, 0, 'Nama Pembeli')
        sheet.write(4, 1, 'Tgl. Order')
        sheet.write(4, 2, 'Total Pembayaran')
        sheet.write(4, 3, 'Status')
        row = 4
        col = 0

        for obj in order:
            col += 0
            report_name = obj.name
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.nama_pembeli)
            sheet.write(row, col+2, obj.tgl_order)
            sheet.write(row, col+3, obj.total_bayar)
            for loop in obj.daftarmobil_id:
                sheet.write(row, col+4, loop.name)
                col += 0
                row += 1
            