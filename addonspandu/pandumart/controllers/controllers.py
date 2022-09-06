from odoo import http, models, fields
from odoo.http import request
import json

class Pandumart(http.Controller):
    @http.route('/pandumart/getbarang', auth= 'public', method=['GET'])
    def getBarang(self, **kw):
        barang = request.env['pandumart.barang'].search([])
        isi = []
        for bb in barang:
            isi.append({
                'nama_barang' : bb.name,
                'harga_jual' : bb.harga_jual,
                'stock' : bb.stock
            })
        return json.dumps(isi)

    @http.route('/pandumart/getsupplier', auth='public', method=['GET'] )
    def geSupplier(self, **kw):
        supplier = request.env['pandumart.supplier'].search([])
        supp = []
        for s in supplier:
            supp.append({
                'nama_perusahaan' : s.name,
                'alamat' : s.alamat,
                'no_telepon' : s.no_telp,
                'barang' : s.barang_id[0].name

            })
            return json.dumps(supp)