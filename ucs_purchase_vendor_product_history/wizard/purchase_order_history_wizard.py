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