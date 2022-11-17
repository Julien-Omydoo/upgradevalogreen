# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    sign_and_accept_customized = fields.Char(string="Custom 'Sign & Accept'", default='Sign & Accept')

    review_sign_and_accept_customized = fields.Char(string="Custom Mail 'Review, Accept & Sign Quotation'",
                                                    default='Review, Accept & Sign Quotation')

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        select_type = self.env['ir.config_parameter'].sudo()
        select_type.set_param('custom_sign_and_accept_quotation.sign_and_accept_customized',
                              self.sign_and_accept_customized)
        select_type.set_param('custom_sign_and_accept_quotation.review_sign_and_accept_customized',
                              self.review_sign_and_accept_customized)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        select_type = self.env['ir.config_parameter'].sudo()
        sac = select_type.get_param('custom_sign_and_accept_quotation.sign_and_accept_customized')
        rsac = select_type.get_param('custom_sign_and_accept_quotation.review_sign_and_accept_customized')
        res.update({
            'sign_and_accept_customized': sac or 'Accept & Sign',
            'review_sign_and_accept_customized': rsac or 'Review, Accept & Sign Quotation'
        })
        return res
