# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'POS Display gross price on products',
    'version': '10.0.1.0.0',
    'category': 'Point Of Sale',
    'sequence': 1,
    'author': "Callino,"
              "Odoo Community Association (OCA)",
    'summary': 'Gross price on PoS Products',
    'license': 'AGPL-3',
    'depends': [
        'point_of_sale',
    ],
    'data': [
        'views/assets.xml',
    ],
    'qweb': [
        'static/src/xml/productscreen.xml',
    ],
    'installable': True,
}
