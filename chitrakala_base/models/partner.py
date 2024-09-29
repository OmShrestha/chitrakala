from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_artist = fields.Boolean(string='Artist')
    