# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    confirm_user_id= fields.Many2one('res.users', string='Confirmed User')

    def action_confirm(self):
        print("================success inherit function============") #task1
        super(SaleOrder, self).action_confirm() #task2
        self.confirm_user_id= self.env.user.id