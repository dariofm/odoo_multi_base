# -*- coding: utf-8 -*-
# Copyright 2016, 2017 Openworx
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Backend Theme",
    "summary": "Odoo 11.0 community backend theme",
    "version": "11.0.1.0.1",
    "category": "Backend Tema",
    "website": "",
	"description": """
		Backend theme for Odoo 11.0 community edition.
    """,
	'images':[
        'images/screen.png'
	],
    "author": "ADAX Technology",
    "license": "LGPL-3",
    "installable": True,
    'auto_install': True,
    "depends": [
        'web_responsive',
    ],
    "data": [
        'views/assets.xml',
        'views/res_company_view.xml',
    ],
}

