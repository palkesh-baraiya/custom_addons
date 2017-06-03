# -*- encoding: utf-8 -*-

{
    'name': 'Pathology Laboratory',
    'author': 'axilt',
    'version': '1.0',
    'depends': [
        'sale',
    ],
    'category' : 'Tools',
    'summary': 'Pathology Laboratory System',
    'description': """ """,
    'data': [
        'laboratory.xml',
        'demo_data.xml',
        'lab_report.xml',
        'views/report_laboratory.xml',
        'security/laboratory_security.xml',
        'security/ir.model.access.csv',

    ],
    'demo': [],
    'installable': True,
    'application': True
}
