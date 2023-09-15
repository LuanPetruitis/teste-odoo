# -*- coding: utf-8 -*-
{
    "name": "Integração de faturas",
    "version": "1.0",
    "sumary": """
        Permite a integração de faturas com o sistema financeiro externo
    """,
    "description": "Permite a integração de faturas com o sistema financeiro externo",
    "author": "Luan",
    "category": "account",
    "depends": ["account"],
    "data": [
        'security/ir.model.access.csv',

        'views/account_invoice_integration.xml',
    ],
    "installable": True,
    "application": True,
}
