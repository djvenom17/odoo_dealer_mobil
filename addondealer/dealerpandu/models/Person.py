from odoo import api, fields, models


class Person(models.Model):
    _name = 'dealerpandu.person'
    _description = 'New Description'

    name = fields.Char(string='Name')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Date(string='Tgl Lahir')
    plat_mobil = fields.Char(string='Plat Mobil')


class Karyawan(models.Model):
    _name = 'dealerpandu.karyawan'
    _inherit = 'dealerpandu.person'
    _description = 'New Description'

    employee_junior = fields.Boolean('Junior')
    employee_senior = fields.Boolean('Senior')

    
    
    
