# -*- coding: utf-8 -*-
{
    'name': "dealerpandu",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'fleet', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu_view.xml',
        'views/daftarmobil_view.xml',
        'views/brandmobil_view.xml',
        'views/fleet_view.xml',
        'views/person_view.xml',
        # 'views/karyawan_view.xml',
        'views/junior_view.xml',
        'views/senior_view.xml',
        'views/dealermitra_view.xml',
        'views/order_view.xml',
        'wizard/addmobil_wizard_view.xml',
        'report/report.xml'
        
        

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
