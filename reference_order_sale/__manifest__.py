{
    'name': 'Reference Order Sale',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Add Code Reference to Sales Orders',
    'description': """
        Task 1:
        - Add a custom field (code_reference) to Sale Order.
        - Display it after the Quotation Date.
    """,
    'author': 'Ashraf Talal',
    'depends': ['sale_management'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
