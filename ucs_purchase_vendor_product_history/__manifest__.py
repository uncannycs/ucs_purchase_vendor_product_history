# -*- coding: utf-8 -*-
{
    'name': "Purchase History Of Products",
    'version': '19.0.1.0.0',
    'summary': """User can view The Purchase history of The 
    products from Purchase Order Line""",
    'description': """Purchases history of products from Purchase Order Line""",
    'author': "Cybrosys Techno Solutions",
    'company': "Cybrosys Techno Solutions",
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'category': 'Purchase/Purchase',
    'depends': ['base','purchase'],
    'license': 'AGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'wizard/product_purchase_order_history_wizard_views.xml',
        'views/purchase_order_view.xml',
    ],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'auto_install': False,
    "price": 25,
}

