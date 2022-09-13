from odoo import api, fields, models


class Person(models.Model):
    _name = 'pandumart.person'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Date(string='Tanggal Lahir')

class Kasir(models.Model):
    _name = 'pandumart.kasir'
    _inherit = 'pandumart.person'
    _description = 'New Description'

    id_kasir = fields.Char(string='ID Kasir')


class CleaningService(models.Model):
    _name = 'pandumart.cleaningservice'
    _inherit = 'pandumart.person'
    _description = 'New Description'

    id_cln = fields.Char(string='ID CLeaning Service')

   

    
    
