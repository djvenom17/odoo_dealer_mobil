from odoo import api, fields, models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.dealerpandu.report_order_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, order):
        sheet = workbook.add_worksheet('Daftar Order History')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'Nota Number')
        sheet.write(1, 1, 'Nama Pembeli')
        sheet.write(1, 2, 'Tgl. Order')
        sheet.write(1, 3, 'Total Pembayaran')
        sheet.write(1, 3, 'Status')
        row = 2
        col = 0

        for obj in order:
            row += 1
            report_name = obj.name
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.nama_pembeli.display_name)
            sheet.write(row, col+2, obj.tgl_order)
            sheet.write(row, col+3, obj.total_bayar)
            sheet.write(row, col+3, obj.state)
            