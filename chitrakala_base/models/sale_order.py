from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    chitrakala_status = fields.Selection([('unassigned', 'Unassigned'),
                                          ('assigned', 'Artist Assigned'),
                                          ('completed', 'Art Completed'), 
                                          ('dispatched', 'Dispatched'),
                                          ('delivered', 'Delivered')],
                                           required=True,
                                           string="Art Status",
                                           tracking=1,
                                           default='unassigned')
    art_by = fields.Many2one('res.partner', string="Artist")

    #order details fields

    no_of_people = fields.Integer(string='No. Of People')
    art_type = fields.Many2one('art.type', string="Art Type")
    art_size = fields.Many2one('paper.size', string="Size")
    is_framed = fields.Boolean(string="Framing")
    order_urgency = fields.Many2one('order.urgency', string="Urgency")
    delivery_type = fields.Many2one('delivery.type', string="Delivery Type")


    # art tracking

    artist_assigned_date = fields.Datetime(string='Assigned Date')
    art_completed_date = fields.Datetime(string="Completed Date")
    art_dispatched_date = fields.Datetime(string="Dispatched Date")
    art_delivered_date = fields.Datetime(string="Delivered Date")

    #profit estimations

    artist_fee = fields.Float(string="Artist Fee")
    gross_profit = fields.Float(string="Gross Profit", compute="_calculate_art_profits", store='True')
    

    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        if 'art_by' in vals:
            self.chitrakala_status = 'assigned'
            self.artist_assigned_date = datetime.now()
        return res

    def action_complete_artwork(self):
        if self.chitrakala_status == 'assigned':
            self.chitrakala_status = 'completed'
            self.art_completed_date = datetime.now()
        else:
            raise ValidationError('Art piece cannot be completed before assigning artist')
        
    def action_dispatch_artwork(self):
        if self.chitrakala_status == 'completed':
            self.chitrakala_status = 'dispatched'
            self.art_dispatched_date = datetime.now()
        else:
            raise ValidationError('Art piece cannot be dispatched before complition')
    
    def action_deliver_artwork(self):
        if self.chitrakala_status == 'dispatched':
            self.chitrakala_status = 'delivered'
            self.art_delivered_date = datetime.now()
        else:
            raise ValidationError('Art piece cannot be delivered before dispatch')
    
    @api.depends('amount_total', 'artist_fee')
    def _calculate_art_profits(self):
        for res in self:
            if res.amount_total and res.artist_fee:
                res.gross_profit = res.amount_total - res.artist_fee
            else:
                res.gross_profit = 0