# -*- coding: utf-8 -*-
{
    'name': "Indicadores Financieros SIEMPRE®",

    'summary': """
        Interfaz del Modulo de Indicadores Financieros SIEMPRE®""",

    'description': """
        Vistas de Tablas y Graficas de los Indicadores Financieros del Sistema Integrado Especializado en el Manejo y Planificación de Recursos Empresariales SIEMPRE® 
    """,

    'author': "Jairo Martinez",
    'website': "http://www.siempresistemas.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Indicadores Financieros',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','siempre','website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',

        'static/src/xml/inicio_indicador.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
}