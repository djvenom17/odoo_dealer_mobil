from odoo import api, fields, models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.dealerpandu.report_daftarmobil_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, daftarmobil):
        sheet = workbook.add_worksheet('Daftar Mobil')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'Nama Mobil')
        sheet.write(1, 1, 'Harga Modal Mobil')
        sheet.write(1, 2, 'Harga Jual Mobil')
        sheet.write(1, 3, 'Stock Mobil')
        sheet.write(1, 4, 'Brand Mobil')
        row = 2
        col = 0

        for obj in daftarmobil:
            col = 0
            report_name = obj.name
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.harga_mobil_modal)
            sheet.write(row, col+2, obj.harga_mobil_jual)
            sheet.write(row, col+3, obj.stock)
            for loop in obj.brandmobil_id:
                sheet.write(row, col+4, loop.name)
                col += 1
                row += 1