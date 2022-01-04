from odoo import models, fields, api

class SalesOrderExpand(models.Model):
    _name = "purchase.order"
    _inherit = ["purchase.order"]



    reserve_date1 = fields.Datetime(string='reserve_date1', help="reserve date1 ")
    reserve_date2 = fields.Datetime(string='reserve_date2', help="reserve date2.")
    reserve_date3 = fields.Datetime(string='reserve_date3', help="reserve date3.")
