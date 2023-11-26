

{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'summary': 'Hospital Management System',
    'description': 'Hospitl management system',
    'depends': ['base','mail'],
    'data':[
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'security/ir.model.access.csv',
    ],
    'application':True,
    'sequence':-1,
    'installable': True,
    'auto_install': False,
    'assets':{},
    'author': 'Ade Setiawan',
    'website': 'digitalfarmer.github.io',
    'license': 'LGPL-3',

}