from odoo import models, fields

class SaleOrder(models.Model):
    """
    Extending the Sales Order model to add custom tracking fields.
    Part of Task 1: Custom Reference Field Implementation.
    """
    _inherit = 'sale.order'

    # Custom field to store an additional reference code for the order
    # help: provides a tooltip for users in the UI
    code_reference = fields.Char(
        string="Code Reference",
        help="Custom reference code for this sales order."
    )