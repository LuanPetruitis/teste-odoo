#-*- coding: utf-8 -*-
import json

import requests
from odoo import api, fields, models
from odoo.exceptions import ValidationError

TIMEOUT = 20

INVOICE_API_BASE_URL = 'http://localhost:8000'


class AccountMoveInherit(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        res = super(AccountMoveInherit, self).action_post()

        response = requests.post(
            INVOICE_API_BASE_URL,
            data=json.dumps(self.read()[0], default=str),
            timeout=TIMEOUT
        )
        if response.status_code not in [200, 201]:
            values = {
                "invoice_id": self.id,
                "external_system_id": "",
                "status": "error",
                "response_message": response.text
            }
        else:
            values = {
                "invoice_id": self.id,
                "external_system_id": json.loads(response.text).get("id"),
                "status": "success",
                "response_message": response.text
            }

        self.env["account.invoice.integration"].create(values)

        return res
