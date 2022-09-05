from xml.dom import ValidationErr
from odoo import api, fields, models
from odoo.exceptions import ValidationError



class Penjualan(models.Model):
    _name = 'pandumart.penjualan'
    _description = 'New Description'

    name = fields.Char(string='No. Nota')
    nama_pembeli = fields.Char(string='Nama Pembeli')
    tgl_penjualan = fields.Datetime(string='Tgl. Transaksi', default = fields.Datetime.now())
    total_bayar = fields.Integer(compute='_compute_totalbayar', string='Total Pembayaran')
    detailpenjualan_ids = fields.One2many(comodel_name='pandumart.detailpenjualan', 
                                          inverse_name='penjualan_id', 
                                          string='Detail Penjualan')
    
    @api.depends('detailpenjualan_ids')
    def _compute_totalbayar(self):
        for rec in self:
            a = sum(self.env['pandumart.detailpenjualan'].search([('penjualan_id','=',rec.id)]).mapped('subtotal'))
            rec.total_bayar = a

    # @api.ondelete(at_uninstall=False)
    # def __ondelete_penjualan(self):
    #     if self.detailpenjualan_ids:
    #         a=[]
    #         for rec in self:
    #             a = self.env['pandumart.detailpenjualan'].search([('penjualan_id','=',rec.id)])
    #             print(a)
    #         for ob in a:
    #             print(str(ob.barang_id.name) + ' ' + str(ob.qty))
    #             ob.barang_id.stock += ob.qty

    #methode UNLINK/ONDELETE untuk ODOO14 (menghapus barang)
    def unlink(self):
        if self.detailpenjualan_ids:
            a = []
            for rec in self:
                a = self.env['pandumart.detailpenjualan'].search([('penjualan_id','=',rec.id)])
                print(a)
            for ob in a:
                print(str(ob.barang_id.name) + ' ' + str(ob.qty))
                ob.barang_id.stock += ob.qty
        record = super(Penjualan,self).unlink()

    #method write
    def write(self, vals):
        for rec in self:
            a= self.env['pandumart.detailpenjualan'].search([('penjualan_id','=',rec.id)])
            print(a)
            for data in a:
                print(str(data.barang_id.name)+' '+str(data.qty)+' '+str(data.barang_id.stock))
                data.barang_id.stock += data.qty
        record = super(Penjualan, self).write(vals)
        for rec in self:
            b= self.env['pandumart.detailpenjualan'].search([('penjualan_id','=',rec.id)])
            print(b)
            for databaru in b:
                if databaru in a:   
                    print(str(databaru.barang_id.name)+' '+str(databaru.qty)+' '+str(databaru.barang_id.stock))
                    databaru.barang_id.stock -= databaru.qty
                else:
                    pass
        return record 

    #contoh struktur SQL CONSTRAINTS (pembatasan/exception dalam penginputan)
    #sql cons diterapkan untuk tabel dan berlaku ketika tabel di panggil kemanapun
    # _sql_constraints = [
    #   (<nama constraints>,<constraintsnya>,<pesan constraints>)
    # ]

    #contoh SQL Constraints
    _sql_constraints = [
        ('no_nota_unik','unique (name)','Nomor Nota Tidak Boleh Sama !!!')
        ]

    

class DetailPenjualan(models.Model):
    _name = 'pandumart.detailpenjualan'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    penjualan_id = fields.Many2one(comodel_name='pandumart.penjualan', string='Detail Penjualan')
    barang_id = fields.Many2one(comodel_name='pandumart.barang', string='List Barang')
    
    harga_satuan = fields.Integer(string='Harga Satuan')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')
    
    @api.depends('harga_satuan', 'qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.qty * rec.harga_satuan

    @api.onchange('barang_id')
    def _onchange_barang_id(self):
        if (self.barang_id.harga_jual):
            self.harga_satuan = self.barang_id.harga_jual
    
    
    @api.model
    def create(self,vals):
        record = super(DetailPenjualan,self).create(vals)
        if record.qty:
            self.env['pandumart.barang'].search([('id','=',record.barang_id.id)]).write({'stock' : record.barang_id.stock - record.qty})
        return record

    #contoh python constrains
    #python cons hanya berlaku di program saja bukan pada tabel databasenya
    @api.constrains('qty')
    def check_quantity(self):
        for rec in self:
            if rec.qty < 1 :
                raise ValidationError('Mau Belanja {} berapa banyak sih...'.format(rec.barang_id.name))
            elif (rec.barang_id.stock < rec.qty):
                raise ValidationError('stock {} tidak mencukupi, hanya tersedia {}'.format(rec.barang_id.name, rec.barang_id.stock))
    
    # _sql_constraints = [
    #     ('qty_wrong','CHECK(qty < 1)','qty kocak geming ajib')
    #     ]