# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Check In-Out',
    'author': 'Afe',
    'version': '1.0',
    'category': 'Human Resources',
    'sequence': 81,
    'summary': 'rekap data absensi',
    'description': """""",
    'depends': ['hr', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_checkinout_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
