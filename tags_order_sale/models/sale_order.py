from odoo import models, fields

class SaleOrder(models.Model):
    """ Extend Sale Order to link with the custom tagging system """
    _inherit = 'sale.order'

    # Many2many relationship linking Sales Orders to custom Tags (Task 2)
    tag_ids = fields.Many2many(
        'sale.tag',
        string='Tags',
        help="Select tags for this sales order"
    )