from odoo import models, fields


class SaleTag(models.Model):
    """ New model to manage custom tags for Sales Orders (Task 2) """
    _name = 'sale.tag'
    _description = 'Sales Order Tag'

    # Required field with translation support for multi-language environments
    name = fields.Char(string='Name', required=True, translate=True)

    # Optional field for additional tag information
    description = fields.Text(string='Description')

    # Used by many2many_tags widget for UI color decoration
    color = fields.Integer(string='Color')