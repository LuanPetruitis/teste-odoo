#-*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountInvoiceIntegration(models.Model):
    _name = 'account.invoice.integration'
    _description = u'Para integração de faturas'

    invoice_id = fields.Many2one("account.move", string="Fatura")
    external_system_id = fields.Char(string="ID externo", help="ID da fatura no sistema externo")
    status = fields.Selection([
        ('peding', 'Pendente'),
        ('success', 'Sucesso'),
        ('error', 'Erro'),
    ], string="Status")
    response_message = fields.Text(string="Resposta", help="Mensagem de resposta do sistema externo")
