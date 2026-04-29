{
    'name': 'Inventario Visual Estilizado',
    'version': '1.6',
    'summary': 'Control de objetos por lugar, estado y cantidad',
    'category': 'Tools',
    'author': 'RafaGuil',
    'depends': ['base', 'web_hierarchy'],
    'data': [
        'security/ir.model.access.csv',
        'views/storage_view.xml',
    ],
    'installable': True,
    'application': True,
}