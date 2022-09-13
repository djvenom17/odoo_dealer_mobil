from odoo import api, fields, models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.res.report_senior_xlsx_template'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, partner):
        sheet = workbook.add_worksheet('Daftar Junior Employee')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'Nama')
        sheet.write(1, 1, 'Phone')
        sheet.write(1, 2, 'email')
        sheet.write(1, 3, 'Plat Mobil')
        sheet.write(1, 4, 'Junior')
        sheet.write(1, 5, 'Senior')
        row = 2
        col = 0

        for obj in partner:
            row += 1
            sheet.write(row, col, obj.display_name)
            sheet.write(row, col+1, obj.phone)
            sheet.write(row, col+2, obj.email)
            sheet.write(row, col+3, obj.plat_mobil)
            sheet.write(row, col+4, obj.employee_junior)
            sheet.write(row, col+5, obj.employee_senior)
            
            