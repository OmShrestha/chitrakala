# -*- coding: utf-8 -*-
{
    'name': "Chitra Kala",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Kinnmel",
    'website': "https://www.kinnmel.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','product','sale'],

    # always loaded
    'data': [
        # 'security/multi_vendor_groups.xml',
        # 'security/kinnmel_security_group.xml',
        'security/ir.model.access.csv',
        'views/sale_order.xml',
        'views/partner.xml',
        'views/art_type.xml',
        'views/paper_size.xml',
        'views/urgency.xml',
        'views/delivery.xml',
    ],

}

