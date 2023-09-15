#-*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'


    @api.depends('invoice_line_ids', 'currency_id', 'amount_total')
    def _compute_total_converted(self):
        for record in self:
            if self.env.user.company_id.currency_id.id != record.currency_id.id:
                exchange_id = self.env['account.foreign.exchange.rate'].search([
                    ('currency_from_id', '=', record.currency_id.id),
                    ("currency_to_id", "=", self.env.user.company_id.currency_id.id)
                ], limit=1)
                if exchange_id:
                    record.total_converted = record.amount_total * exchange_id.exchange_rate
                else:
                    record.total_converted = 0
            else:
                record.total_converted = 0

    total_converted = fields.Float(string="Total Convertido", help="Valor total convertido para moeda base da empresa.", compute='_compute_total_converted', store=True)
