from odoo import api, fields, models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.dealerpandu.report_brandmobil_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, brandmobil):
        sheet = workbook.add_worksheet('Daftar Mobil')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'Nama Brand')
        sheet.write(1, 1, 'Founder Brand')
        sheet.write(1, 2, 'Brand Country')
        sheet.write(1, 3, 'Jumlah Tipe Mobil')
        sheet.write(1, 4, 'Daftar Mobil')
        row = 2
        col = 0

        for obj in brandmobil:
            row += 1
            report_name = obj.name
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.founder_brand)
            sheet.write(row, col+2, obj.brand_country)
            sheet.write(row, col+3, obj.jml_mobil)
            sheet.write(row, col+4, obj.daftar)

            