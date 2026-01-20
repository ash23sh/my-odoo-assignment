# Odoo Custom Sales Integration

## Features
- **Task 1:** Added `code_reference` to Sales Orders.
- **Task 2:** Created a new Tagging system (`sale.tag`) with M2M relationship in Sales.
- **Task 3:** Implemented Price Controls on Product Template with validation on Sales Order confirmation.

## Technical Details
- **Security:** Access rights restricted to 'Sales Managers' for price settings.
- **Validation:** Python constraints prevent logical errors (Min > Max).
- **UI/UX:** Used `monetary` widgets and `xpath` inheritance for a seamless user experience.

## Installation
1. Install `reference_order_sale`.
2. Install `tags_order_sale`.
3. Install `sale_price_control`.