# -*- coding: utf-8 -*-
{
    'name': "SimpleContact",

    'summary': "Simple contact management ",

    'description': """
Long description of module's purpose
    """,

    'author': "Urvish",
    'website': "http://localhost",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Contact',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/FieldViews.xml',
        'views/Menu_and_Action.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    'demo/demo.xml',
    ],
}

