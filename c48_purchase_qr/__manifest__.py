# -*- coding: utf-8 -*-
{
    "name": "Purchase Order QR",
    "summary": """Purchase Order QR Code""",
    'author': "Core48 ",
    'website': "https://core48.com",
    'category': 'Purchase Management',
    "version": "17.0.0.1",
    'license': 'LGPL-3',
    "depends": [
        'purchase'
            ],
    "data": [
        "views/inherit_purchase.xml",
        "views/inherit_report.xml" 
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    "images": ["static/description/banner.jpg"],

}
