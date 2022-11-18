# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    sign_and_accept_customized = fields.Char(string="Custom 'Sign & Accept'",
                                             compute='compute_sign_and_accept_customized', readonly=True)

    review_sign_and_accept_customized = fields.Char(string="Custom 'Review, Accept & Sign Quotation'",
                                                    compute='compute_review_sign_and_accept_customized', readonly=True)

    def compute_sign_and_accept_customized(self):
        for record in self:
            if self.env['ir.config_parameter'].sudo().get_param(
                    'custom_sign_and_accept_quotation.sign_and_accept_customized'):
                record.sign_and_accept_customized = self.env['ir.config_parameter'].sudo().get_param(
                    'custom_sign_and_accept_quotation.sign_and_accept_customized')
            else:
                record.sign_and_accept_customized = 'Sign & Accept'

    def compute_review_sign_and_accept_customized(self):
        for record in self:
            if self.env['ir.config_parameter'].sudo().get_param(
                    'custom_sign_and_accept_quotation.sign_and_accept_customized'):
                record.review_sign_and_accept_customized = self.env['ir.config_parameter'].sudo().get_param(
                    'custom_sign_and_accept_quotation.review_sign_and_accept_customized')
            else:
                record.review_sign_and_accept_customized = 'Review, Accept & Sign Quotation'
