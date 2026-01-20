from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        """
        Override the action_confirm method to validate line prices
        against product minimum and maximum sale price constraints.
        """
        for order in self:
            for line in order.order_line:
                # Get the product template associated with the sale order line
                product = line.product_id

                # Check if a Minimum Sale Price is set and if the unit price is below it
                if product.min_sale_price > 0 and line.price_unit < product.min_sale_price:
                    raise ValidationError(
                        f"Price Validation Error:\n"
                        f"Product: {product.name}\n"
                        f"Unit Price: {line.price_unit}\n"
                        f"The price is below the allowed minimum of {product.min_sale_price}."
                    )

                # Check if a Maximum Sale Price is set and if the unit price is above it
                if product.max_sale_price > 0 and line.price_unit > product.max_sale_price:
                    raise ValidationError(
                        f"Price Validation Error:\n"
                        f"Product: {product.name}\n"
                        f"Unit Price: {line.price_unit}\n"
                        f"The price exceeds the allowed maximum of {product.max_sale_price}."
                    )

        # If all line validations pass, proceed with the standard confirmation process
        return super(SaleOrder, self).action_confirm()