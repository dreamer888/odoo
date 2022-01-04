{
    'name': "sales expand",
    'summary': """
        sales expand
    """,
    'description': """
        sales expand 
    """,
    'author': "dreamer",
    'website': "http://www.dreammm.net",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'sales expand',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['sale', 'sale_management'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/view.xml',
        'views/expand_view.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
