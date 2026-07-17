# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Vishnu KP @ Cybrosys, (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    def get_purchase_product_history_data(self):
        
         # It returns the product history data
        values = []
        ovalues = []
        customer_id = self.order_id.partner_id
        customer_order = self.env['purchase.order'].search(
            [('id','!=',self.order_id.id), ('partner_id', '=', customer_id.id),
                ('state', 'not in', ('cancel', 'refuse'))], order="date_order desc")
        customer_order_other = self.env['purchase.order'].search(
            [('id','!=',self.order_id.id), ('partner_id', '!=', customer_id.id), ('state', 'not in', ('cancel', 'refuse'))], order="date_order desc")
        
        for order in customer_order:
            for line in order.order_line:
                if line.product_id == self.product_id:
                    values.append((0, 0, {'purchase_order_id': order.id,
                                          'history_price': line.price_unit,
                                          'history_qty': line.product_uom_qty,
                                          'history_total': order.amount_total
                                          }))
        for oorder in customer_order_other:
            for oline in oorder.order_line:
                if oline.product_id == self.product_id:
                        ovalues.append((0, 0, {'purchase_order_id': oorder.id,
                                               'partner_id': oorder.partner_id.id,
                                              'history_price': oline.price_unit,
                                              'history_qty': oline.product_uom_qty,
                                              'history_total': oorder.amount_total
                                              }))
        history_id = self.env['product.purchase.order.history'].create({
            'product_id': self.product_id.id,
            'product_purchase_history_ids': values, 'product_purchase_ohistory_ids':ovalues})
        

        return {
            'name': 'Customer Product Purchase History',
            'view_mode': 'form',
            'res_model': 'product.purchase.order.history',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'res_id': history_id.id 
        }
      
