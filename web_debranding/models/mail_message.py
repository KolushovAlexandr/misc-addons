# -*- coding: utf-8 -*-
import logging
from odoo import models

from .ir_translation import debrand

_logger = logging.getLogger(__name__)

MODULE = '_web_debranding'


class MailMessage(models.Model):
    _inherit = 'mail.message'

    def create(self, values):
        subject = values.get('subject')
        channel_all_employees = self.env.ref('mail.channel_all_employees', raise_if_not_found=False)
        if channel_all_employees \
           and subject \
           and valus.get('model') == 'mail.channel' \    
           and channel_all_employees.id == values.get('res_id') \
           and subject.endswith('application installed!'):
            values['body'] = debrand(self.env, values.get('body', ''), is_code=False)
        return = super(MailMessage, self).create(values)
