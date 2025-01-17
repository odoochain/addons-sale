# Copyright 2022 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import api, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.onchange("type_id")
    def onchange_type_id(self):
        result = super().onchange_type_id()
        for order in self:
            if order.type_id and order.type_id.carrier_id:
                order.carrier_id = order.type_id.carrier_id.id
        return result
