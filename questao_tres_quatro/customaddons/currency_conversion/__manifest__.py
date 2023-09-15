# -*- coding: utf-8 -*-
{
    "name": "Conversão de Moedas",
    "version": "1.0",
    "sumary": """
        Módulo para converter a moeda da empresa para outras moedas
    """,
    "description": "Módulo para converter a moeda da empresa para outras moedas",
    "author": "Luan",
    "category": "account",
    "depends": ["account"],
    "data": [
        'security/ir.model.access.csv',

        'views/account_foreign_exchange_rate.xml',
        'views/account_move.xml',
    ],
    "installable": True,
    "application": True,
}
