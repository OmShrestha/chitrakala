from odoo import models, fields, api
from datetime import datetime


class ArtType(models.Model):
    _name = 'art.type'
    _description = 'Art Types'


    name = fields.Char(string="Name", required=True)
    description = fields.Html(string="Description")



class PaperSize(models.Model):
    _name = 'paper.size'
    _description = "Art Paper Size"

    name = fields.Char(string="Name", required=True)
    width = fields.Float(string="Width")
    height = fields.Float(string="Height")

