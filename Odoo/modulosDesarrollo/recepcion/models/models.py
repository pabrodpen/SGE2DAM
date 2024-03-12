from odoo import models, fields, api

class recepcion_checkin(models.Model):
    _name = 'recepcion.checkin'
    _description = 'checkin'
    
    
    guest_name = fields.Char(string="Nombre", required=True, help="Introduce el título de la película")
    checkin_date = fields.Date(string="Fecha entrada", required=True, help="Introduce el director")
    checkout_date = fields.Date(string="Fecha salida")
    room_id = fields.Integer(string="ID")
    room_type = fields.Selection([('0','Standard'),('1','Deluxe'),('2','Suite')], default='0',string="Tipo")
    price_per_day = fields.Float(string="Precio diario")
    total_price = fields.Float(string="Precio total",compute="_value_precio",store=True)

    

     @api.depends('total_price','checkin_date','checkout_date')
     def _value_precio(self):
         for record in self:
             rdo=(record.checkin_date-record.checkout_date).days
             record.total_price=record.price_per_day*rdo

