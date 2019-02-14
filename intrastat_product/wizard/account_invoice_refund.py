# -*- coding: utf-8 -*-

from odoo import models, api


class AccountInvoiceRefund(models.TransientModel):
    _inherit = "account.invoice.refund"

    @api.multi
    def invoice_refund(self):
        # we pass on this method invoice_refund so
        # the context type should be change to 'out_refund'.
        # with that the account_invoice._default_intrastat_transaction_id()
        # have right context to set the proper intrastat_transaction_id
        ctx = self._context.copy()
        ctx.update({'type': u'out_refund'})
        return super(
            AccountInvoiceRefund, self.with_context(ctx)
        ).invoice_refund()
