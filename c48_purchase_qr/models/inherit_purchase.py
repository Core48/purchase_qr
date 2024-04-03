from odoo import fields, models


class InheritQuotatins(models.Model):
    _inherit = 'purchase.order'

    qr = fields.Binary(string='QR')
