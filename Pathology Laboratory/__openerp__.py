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
        'views/laboratory.xml',
        'views/demo_data.xml',
        'lab_report.xml',
        'report/report_laboratory.xml',
        'security/laboratory_security.xml',
        'security/ir.model.access.csv',

    ],
    'demo': [],
    'installable': True,
    'application': True
}
