from odoo import models, fields, api

class AuthProduct(models.Model):
    _name = "auth.product"

    project_name = fields.Char(string='项目名称', required=True)

    is_authed = fields.Boolean(string='已经认证', help="是否已经认证过了")

    partner_id = fields.Many2one(comodel_name='res.partner', string='联系人')

    reserve_date1 = fields.Datetime(string='到期时间',  index=True,  help="reserve date1 ")
    auth_company_name = fields.Char(string='认证公司名称', required=False, index=True)
    people_amount = fields.Char(string='公司人数', required=False)
    is_high_tech = fields.Boolean(string='是否高新企业', help="是否高新")






class ContactExpand(models.Model):
    #_name = "res.partner"
    _inherit = ["res.partner"]

    industry = fields.Char(string='公司行业', required=False)
    project_scope = fields.Char(string='认证范围', required=False)
    is_need_train = fields.Boolean(string='需要内审培 训', help="是否需要内审培训")
    is_high_tech = fields.Boolean(string='是否高新企业', help="是否高新")

    #product_id = fields.Many2one('auth.product', string="认证产品", ondelete='cascade', required=False,index=True,help="....")

    #project_parent_id = fields.Many2one('auth.product', string='Related project', index=True)
    project_child_ids = fields.One2many(comodel_name='auth.product', inverse_name='partner_id', string='projects')


    image = fields.Image()
    #image = fields.Binary('图片')
    image_256 = fields.Image("Image 256", related='image', max_width=256, max_height=256, store=True, readonly=False)
    image_512 = fields.Image("Image 512", related='image', max_width=512, max_height=512, store=True, readonly=False)
    image_1024 = fields.Image("Image 1024", related='image', max_width=1024, max_height=1024, store=False, readonly=False)


#################################上传附 件
    attachment_number = fields.Integer(compute='_compute_attachment_number', string='上传附件')


    def _compute_attachment_number(self):
        """附件上传"""
        attachment_data = self.env['ir.attachment'].read_group([('res_model', '=', 'res.partner'), ('res_id', 'in', self.ids)], ['res_id'], ['res_id'])
        attachment = dict((data['res_id'], data['res_id_count']) for data in attachment_data)
        for expense in self:
            expense.attachment_number = attachment.get(expense.id, 0)

    def action_get_attachment_view(self):
        """附件上传动作视图"""
        self.ensure_one()
        res = self.env['ir.actions.act_window'].for_xml_id('base', 'action_attachment')
        res['domain'] = [('res_model', '=', 'res.partner'), ('res_id', 'in', self.ids)]
        res['context'] = {'default_res_model': 'res.partner', 'default_res_id': self.id}
        return re


    def attachment_image_preview(self):
        """附件上传 第二种方式"""
        self.ensure_one()
        # domain可以过滤指定的附件类型 （mimetype）
        domain = [('res_model', '=', self._name), ('res_id', '=', self.id)]
        return {
            'domain': domain,
            'res_model': 'ir.attachment',
            'name': u'附件',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'kanban,tree,form',
            'view_type': 'form',
            'limit': 20,
            'context': "{'default_res_model': '%s','default_res_id': %d}" % (self._name, self.id)
        }




