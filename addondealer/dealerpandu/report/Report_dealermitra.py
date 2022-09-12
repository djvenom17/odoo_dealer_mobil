from odoo import api, fields, models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.dealerpandu.report_dealermitra_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, dealermitra):
        sheet = workbook.add_worksheet('Daftar Dealer Mitra')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(2, 0, 'Nama Dealer')
        sheet.write(2, 1, 'Alamat Dealer')
        sheet.write(2, 2, 'No. Telp')
        sheet.write(2, 3, 'Daftar Mobil')
        row = 3
        col = 0

        for obj in dealermitra:
            col += 0
            report_name = obj.name
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.alamat_dealer)
            sheet.write(row, col+2, obj.no_telp)
            for loop in obj.daftarmobil_id:
                sheet.write(row, col+3, loop.name)
                col += 0
                row += 1
            