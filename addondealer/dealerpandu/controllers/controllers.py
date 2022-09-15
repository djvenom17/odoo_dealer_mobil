from odoo import http, models, fields
from odoo.http import request
import json


class Dealerpandu(http.Controller):
    @http.route('/dealerpandu/getdaftarmobil', auth="public", method=['GET'])
    def getdaftarmobil(self, **kw):
        mobil = request.env['dealerpandu.daftarmobil'].search([])
        isi = []
        for a in mobil:
            isi.append({
                'nama_mobil' : a.name,
                'harga_modal' : a.harga_mobil_modal,
                'harga_jual' : a.harga_mobil_jual,
                'stock' : a.stock,
            })
        return json.dumps(isi)

    @http.route('/dealerpandu/getbrandmobil', auth="public", method=['GET'])
    def getbrandmobil(self, **kw):
        mobil = request.env['dealerpandu.brandmobil'].search([])
        isi = []
        for a in mobil:
            isi.append({
                'nama_mobil' : a.name,
                'founder' : a.founder_brand,
                'jumlah_mobil' : a.jml_mobil,
                'daftar' : a.daftar
            })
        return json.dumps(isi)
    
    @http.route('/dealerpandu/getdealermitra', auth="public", method=['GET'])
    def getdealermitra(self, **kw):
        mitra = request.env['dealerpandu.dealermitra'].search([])
        isi = []
        for a in mitra:
            isi.append({
                'nama_dealer' : a.name,
                'alamat' : a.alamat_dealer,
                'no_telp' : a.no_telp,
            })
        return json.dumps(isi)
    
    @http.route('/dealerpandu/getmembersilver', auth="public", method=['GET'])
    def getmembersilver(self, **kw):
        member = request.env['res.partner'].search([])
        isi = []
        for a in member:
            isi.append({
                'nama' : a.display_name,
                'member_silver' : a.member_silver,
                'member_gold' : a.member_gold
            })
        return json.dumps(isi)

    @http.route('/dealerpandu/getmembergold', auth="public", method=['GET'])
    def getmembergold(self, **kw):
        member = request.env['res.partner'].search([])
        isi = []
        for a in member:
            isi.append({
                'nama' : a.display_name,
                'member_silver' : a.member_silver,
                'member_gold' : a.member_gold
            })
        return json.dumps(isi)


    #res.partner gabisa di json.dumps
    @http.route('/dealerpandu/getorder', auth="public", method=['GET'])
    def getorder(self, **kw):
        order = request.env['dealerpandu.order'].search([])
        isi = []
        for a in order:
            isi.append({
                'nota' : a.name,
                'nama_pembeli' : a.nama_pembeli,
                'tgl' : a.tgl_order,
                'total_bayar' : a.total_bayar,
                
            })
        return json.dumps(isi)
    