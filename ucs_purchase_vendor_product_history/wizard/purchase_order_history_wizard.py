# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
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
from odoo import fields, models


class ProductPurchaseOrderHistory(models.TransientModel):
    _name = 'product.purchase.order.history'
    _description = 'Product Purchase Order History'
    _rec_name = 'product_id'

    product_purchase_history_ids = fields.One2many('product.purchase.history.line',
                                           'order_line_id',
                                           string='Product Purchase Price History',
                                           help="shows the product purchase "
                                                "history of the customer")
    product_id = fields.Many2one('product.product',
                                 string="Product",
                                 help="Choose a Product")
    product_purchase_ohistory_ids = fields.One2many('product.purchase.history.oline',
                                           'order_line_id',
                                           string='Product Purchase Price History generic',
                                           help="shows the product purchase "
                                                "history of the other customer")