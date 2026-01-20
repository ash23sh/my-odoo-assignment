{
    'name': 'Sales Order Tags',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Manage custom tags for Sales Orders',
    'depends': ['sale_management', 'sales_team'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_tag_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}