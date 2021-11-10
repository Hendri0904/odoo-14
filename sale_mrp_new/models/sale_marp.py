# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api,fields,models ,_
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import AccessError, UserError, ValidationError



class InheritSaleOrder(models.Model):
    _inherit = 'sale.order'


    sale_count = fields.Integer(string="MRP", compute='get_mrp_count')
    
    def get_mrp_count(self):
        
        count = self.env['mrp.production']
        count_sale = count.search_count([('sale_id','=', self.id,)])
        self.sale_count = count_sale

    
    def sale_mrp_count(self):
        return{
            'name':_('Sale MRP New'),
            'domain': [('sale_id','=',self.id)],
            'view_type':'form',
            'res_model': 'mrp.production',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }