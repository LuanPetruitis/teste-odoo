#-*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountForeignExchangeRate(models.Model):
    _name = 'account.foreign.exchange.rate'
    _description = u'Para taxa de conversão'
    _rec_name = 'currency_from_id'


    date = fields.Date(string="Data", help="Data da taxa de câmbio")
    currency_from_id = fields.Many2one("res.currency", string="Moeda de origem", help="Moeda de origem")
    currency_to_id = fields.Many2one("res.currency", string="Moeda de destino", help="Moeda de destino")
    exchange_rate = fields.Float(string="Taxa de câmbio", help="Valor da taxa de câmbio")
