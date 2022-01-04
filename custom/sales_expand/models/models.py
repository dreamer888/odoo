from odoo import models, fields, api

class SalesOrderExpand(models.Model):
    _name = "sale.order"
    _inherit = ["sale.order"]

    is_need_train = fields.Boolean(string='需要内审培 训', help="是否需要内审培训")

    reserve_date1 = fields.Datetime(string='reserve_date1', help="reserve date1 ")
    reserve_date2 = fields.Datetime(string='reserve_date2', help="reserve date2.")
    reserve_date3 = fields.Datetime(string='reserve_date3', help="reserve date3.")
