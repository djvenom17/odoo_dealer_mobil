from email.policy import default
from odoo import api, fields, models
from odoo.exceptions import ValidationError



class Order(models.Model):
    _name = 'dealerpandu.order'
    _description = 'New Description'

    name = fields.Char(string='Nota Number', required=True)
    nama_pembeli = fields.Char(string='Nama Pembeli', required=True)
    tgl_order = fields.Date(string='Tgl. Order', default= fields.Datetime.now())
    total_bayar = fields.Integer(compute='_compute_totalorder', string='Total Pembayaran')
    detailorder_ids = fields.One2many(comodel_name='dealerpandu.detailorder', 
                                inverse_name='order_id', 
                                string='Detail Order')
    
    #menghitung total order yang di order oleh pembeli
    @api.depends('detailorder_ids')
    def _compute_totalorder(self):
        for rec in self:
            a = sum(self.env['dealerpandu.detailorder'].search([('order_id','=',rec.id)]).mapped('sub_total'))
            rec.total_bayar = a

    #mengurangi stock (daftarmobil) jika adanya transaksi yang dilakukan di menu (order)
    @api.ondelete(at_uninstall=False)
    def _ondelete_order(self):
        if self.detailorder_ids:
            a=[]
            for rec in self:
                a = self.env['dealerpandu.detailorder'].search([('order_id','=',rec.id)])
            for ob in a:
                ob.daftarmobil_id.stock += ob.qty_order

    #menambahkan lagi (jumlah) order yang dibatalkan kedalam (daftarmobil)
    def write(self, vals):
        for rec in self:
            a= self.env['dealerpandu.detailorder'].search([('order_id','=',rec.id)])
            for data in a:
                data.daftarmobil_id.stock += data.qty_order
        record = super(Order, self).write(vals)
        for rec in self:
            b= self.env['dealerpandu.detailorder'].search([('order_id','=',rec.id)])
            for newdata in b:
                if newdata in a:   
                    newdata.daftarmobil_id.stock -= newdata.qty_order
                else:
                    pass
        return record 

    #SQL Constraints
    _sql_constraints = [
        ('nota_number_unique','UNIQUE (name)','Nomor Nota Tidak Boleh Sama !!!')
        ]

class DetailOrder(models.Model):
    _name = 'dealerpandu.detailorder'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    order_id = fields.Many2one(comodel_name='dealerpandu.order', string='Order ID')
    daftarmobil_id = fields.Many2one(comodel_name='dealerpandu.daftarmobil', string='Daftar Mobil', required=True)
    cost_satuan = fields.Integer(string='Harga Satuan')
    qty_order = fields.Integer(string='Jumlah Pembelian')
    sub_total = fields.Integer(compute='_compute_subtotal', string='Total Harga')    
    
    #jumlah total yang harus dibayarkan
    @api.depends('cost_satuan', 'qty_order')
    def _compute_subtotal(self):
        for rec in self:
            rec.sub_total = rec.qty_order * rec.cost_satuan

    #menampilkan harga mobil satuan
    @api.onchange('daftarmobil_id')
    def _onchange_daftarmobil_id(self):
        if (self.daftarmobil_id.harga_mobil_jual):
            self.cost_satuan = self.daftarmobil_id.harga_mobil_jual
    
    #menampilkan daftarmobil yang tersedia
    @api.model
    def create(self,vals):
        record = super(DetailOrder,self).create(vals)
        if record.qty_order:
            self.env['dealerpandu.daftarmobil'].search([('id','=',record.daftarmobil_id.id)]).write({'stock' : record.daftarmobil_id.stock - record.qty_order})
        return record
    
    #python contraints
    @api.constrains('qty_order')
    def check_quantity_order(self):
        for rec in self:
            if rec.qty_order < 1 :
                raise ValidationError('Isi {} Jumlah yang Ingin Dibeli '.format(rec.daftarmobil_id.name))
            elif (rec.daftarmobil_id.stock < rec.qty_order):
                raise ValidationError('stock {} di gudang tidak mencukupi, hanya tersedia {}'.format(rec.daftarmobil_id.name, rec.daftarmobil_id.stock))
    

