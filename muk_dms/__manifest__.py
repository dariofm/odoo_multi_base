# -*- coding: utf-8 -*-

{
    "name": "MuK Documents",
    "summary": """Document Management System""",
    "description": """ 
        MuK Documents is a module to create, manage and view files
        directly within Odoo. By installing module extensions
        additional features can be enabled.
    """,
    "version": '11.0.1.3.0',   
    "category": 'Document Management',   
    "license": "AGPL-3",
    "website": "http://www.mukit.at",
    "author": "MuK IT",
    "contributors": [
        "Mathias Markl <mathias.markl@mukit.at>",
        "Kerrim Abdelhamed <kerrim.adbelhamed@mukit.at>",
    ],
    "depends": [
        "muk_web_utils",
        "muk_web_preview",
        "muk_web_client_refresh",
    ],
    "data": [
        "security/dms_security.xml",
        "security/ir.model.access.csv",
        "template/assets.xml",
        "views/dms_menu.xml",
        "views/dms_actions.xml",
        "views/dms_settings_view.xml",
        "views/dms_directory_view.xml",
        "views/dms_file_view.xml",
        "views/dms_data_view.xml",
        "views/dms_lock_view.xml",
        "views/res_config_view.xml",
    ],
    "demo": [
        "demo/dms_user_demo.xml",
        "demo/dms_settings_demo.xml",
        "demo/dms_directory_demo.xml",
        "demo/dms_file_demo.xml",
    ],
    "qweb": [
        "static/src/xml/*.xml",
    ],
    "images": [
        'static/description/banner.png'
    ],
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "application": True,
    "installable": True,
}
