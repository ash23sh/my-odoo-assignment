from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Field definitions for minimum and maximum allowed sale prices
    min_sale_price = fields.Float(string='Minimum Sale Price', default=0.0)
    max_sale_price = fields.Float(string='Maximum Sale Price', default=0.0)

    @api.constrains('min_sale_price', 'max_sale_price')
    def _check_price_range(self):
        """
        Constraint Validation:
        This method is automatically triggered by Odoo whenever 'min_sale_price'
        or 'max_sale_price' is saved/updated in the database.
        It ensures that the Minimum price does not logically exceed the Maximum price.
        """
        for record in self:
            # Check if Maximum Price is set (greater than 0) and compare it with Minimum Price
            if record.max_sale_price > 0 and record.min_sale_price > record.max_sale_price:
                raise ValidationError(
                    "Configuration Error:\n"
                    "The Minimum Sale Price cannot be greater than the Maximum Sale Price. "
                    "Please verify your price range settings."
                )