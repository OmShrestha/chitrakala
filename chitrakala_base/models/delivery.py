from odoo import models, fields, api
from datetime import datetime


class OrderUrgency(models.Model):
    _name = 'order.urgency'
    _description = "Order Delivery Urgency"

    name = fields.Char(string='Title')


class DeliveryType(models.Model):
    _name = 'delivery.type'
    _description = "Delivery Type"

    name = fields.Char(string="Title")
    