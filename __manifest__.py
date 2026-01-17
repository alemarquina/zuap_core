{
    'name': 'Odoo Zuap',
    'version': '1.0',
    'description': 'Modulo de suscripciones',
    'author': 'Digilab Soluciones',
    'category': 'State',
    'depends': [
        'base',        
        'sale',
        'product',        
        'sale_subscription',
        'account'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/inherit_res_partner.xml'
    ],
    'demo': [

    ],
    'auto_install': True,
    'application': True,      
}