# -*- coding: utf-8 -*-
{
    'name': 'FIT Website Request for Quotation',
    'summary': "Request for Quotation from Website",
    'description': "Request for Quotation from Website",

    'author': 'Fundament IT',
    'website': 'https://fundament.it',
    'support': 'info@fundament.it',

    'category': 'eCommerce',
    'version': '12.0.0.1.0',
    'depends': ['website_sale'],

    'data': [
        'views/product_view.xml',
        'views/template.xml',
        'views/website_quotation_view.xml',
    ],

    'license': "OPL-1",
    'price': 59,
    'currency': "EUR",

    'auto_install': False,
    'installable': True,
}
