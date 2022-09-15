from email.policy import default
from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import datetime



class Order(models.Model):
    _name = 'dealerpandu.order'
    _description = 'New Description'

    name = fields.Char(string='Nota Number', required=True)
    nama_pembeli = fields.Many2one(comodel_name="res.partner",string='Nama Pembeli', required=True)
    tgl_order = fields.Datetime(string='Tgl. Order')
    total_bayar = fields.Integer(compute='_compute_totalorder', string='Total Pembayaran')
    detailorder_ids = fields.One2many(comodel_name='dealerpandu.detailorder', 
                                inverse_name='order_id', 
                                string='Detail Order')
    state = fields.Selection(string='Status', 
                             selection=[('draft', 'Draft'), 
                                        ('confirm', 'Confirm'),
                                        ('done', 'Done'),
                                        ('cancel', 'Cancel')],
                            required=True, readonly=True, default="draft") 
    currency_id = fields.Many2one('res.currency', string='Account Currency',
        help="Forces all moves for this account to have this account currency.", required=True)
    member_silver = fields.Boolean(compute='_compute_member_silver',string='Silver')
    member_gold = fields.Boolean(compute='_compute_member_gold',string='Gold')


    @api.depends('nama_pembeli')
    def _compute_member_silver(self):
        for rec in self:
            rec.member_silver = rec.nama_pembeli.member_silver

    @api.depends('nama_pembeli')
    def _compute_member_gold(self):
        for rec in self:
            rec.member_gold = rec.nama_pembeli.member_gold

    #biar tgl. ordernya gak stuck waktunya
    @api.model
    def default_get(self, fields):
        res = super(Order, self).default_get(fields)
        res.update({'tgl_order': datetime.now()})
        return res

    #mengubah state ke confirm
    def action_confirm(self):
        self.write({'state': 'confirm'})

    #mengubah state done
    def action_done(self):
        self.write({'state': 'done'})

    #mengubah state ke cancel
    def action_cancel(self):
        self.write({'state': 'cancel'})

    #mengubah state ke draft
    def action_draft(self):
        self.write({'state': 'draft'})
    

    #menghitung total order yang di order oleh pembeli
    @api.depends('detailorder_ids')
    def _compute_totalorder(self):
        for rec in self:
            a = sum(self.env['dealerpandu.detailorder'].search([('order_id','=',rec.id)]).mapped('sub_total'))
            rec.total_bayar = a

    def unlink(self):
        for rec in self:
            #pesan state eror jika action DELETE dilakukan diluar DRAFT
            if rec.filtered(lambda line: line.state != 'draft'):
                raise ValidationError ('tidak dapat menghapus jika status buka DRAFT')
            # mengurangi stock (daftarmobil) jika adanya transaksi yang dilakukan di menu (order)
            if rec.detailorder_ids:
                for data in rec.detailorder_ids:
                    data.daftarmobil_id.stock = data.daftarmobil_id.stock + data.qty_order
        record = super(Order,self).unlink()
        return record

    #menambahkan lagi (jumlah) order yang dibatalkan kedalam (daftarmobil)
    #kalo hapusnya berbarengan eror
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
    order_id = fields.Many2one(comodel_name='dealerpandu.order', string='Order ID', ondelete="cascade")
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
    
    #menghapus qty mobil di M2O daftar mobil
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
    




