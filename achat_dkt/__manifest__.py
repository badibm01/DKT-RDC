# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Achat DKT',
    'version': '1.2',
    'category': 'Achat',
    'sequence': 4,
    'summary': 'stock et achat',
    'website': '',
    'depends': ['hr','purchase','account','account_payment'],
    'data': [
        'security/achat_dkt.xml',       
        'security/ir.model.access.csv',        
        'views/achat_dkt.xml',          
        'data/achat_dkt.xml',
        'report/report.xml',
        'report/AchatDKT.xml',
        
       
        
    ],
    'demo': [
        
    ],
    'installable': True,
    'application': True,
    'assets': {
        
    },
    'license': '',
}
