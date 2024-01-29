# -*- coding: utf-8 -*- 

from odoo import models,fields,api,_
from odoo.exceptions import ValidationError


class QuantPackage(models.Model):
    """ Inherit stock package to allow self parent-child relation for multi-level packaging"""
    _inherit = "stock.quant.package"

    parent_id = fields.Many2one('stock.quant.package', string='Parent Package', index=True)
    child_ids = fields.One2many('hr.department', 'parent_id', string='Child Package')
