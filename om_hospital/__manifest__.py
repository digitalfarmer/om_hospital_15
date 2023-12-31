

{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'summary': 'Hospital Management System',
    'description': 'Hospitl management system',
    'depends': ['base','mail','product'],
    'data':[
        'security/ir.model.access.csv',
        'data/patient.tag.csv',
        'data/sequence_data.xml',
        'wizard/cancel_appointment_view.xml',
        'data/patient_tag_data.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',

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