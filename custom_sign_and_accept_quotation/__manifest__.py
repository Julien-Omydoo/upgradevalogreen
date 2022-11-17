# -*- coding: utf-8 -*-
{
    'name': "Custom 'Review, Sign & Accept' Quotation",

    'summary': """
        Custom 'Review, Sign & Accept' Quotation allows you to choose the text displayed in the customer order
        portal view instead of 'sign & accept' and in the mail view instead of 'review, accept & sign'.
        With this you won't be able to scare your customers anymore.
    """,

    'description': """
        V14.0 - 2022-03-23
        Allows you to choose the text displayed in the customer order
        portal view instead of 'sign & accept' and in the mail view instead of 'review, accept & sign'.
        With this you won't be able to scare your customers anymore.
    """,

    'author': "Omydoo",
    'contributors':["Gabin Neron <gabin@omydoo.fr>"],
    'website': "https://www.omydoo.fr",
    'maintainer': 'Omydoo',
    'category': 'Quotation',
    'version': '14.0',
    'depends': ['base', 'sale'],
    'data': [
        'views/inherit_sale_config_settings_view.xml',
        'views/inherit_sale_order_portal_view.xml',
    ],
    "license": "OPL-1",
    'installable': True,
    'auto_install': False,
    'application': True,
    'active': False,
    'images': ['static/description/custom_s&a_quote.gif'],
    'support': 'support@omydoo.fr',
    'price': 25.00,
    'currency': 'EUR',
}
