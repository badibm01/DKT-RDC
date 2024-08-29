# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.addons.base.models.res_partner import WARNING_MESSAGE, WARNING_HELP
from odoo.tools.float_utils import float_round
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError, AccessError, UserError

READONLY_FIELD_STATES = {
    state: [('readonly', True)]
    for state in {'approuver', 'cancel'}
}





class PurchaseOrder(models.Model):
    
    _inherit = 'purchase.order'

    
    autre_id = fields.One2many('achat.dkt','achat_id','detail')
##    total_facture = fields.Float('Total Facture')
    total_facture = fields.Float(compute='_compute_recurring_tot', string="Total Facture", store=True, tracking=True)
    sous_total =fields.Float ('Sous total')
    bailleur_id = fields.Many2one('bailleur','Bailleur')
    
    @api.depends('autre_id','autre_id.montant')
    def _compute_recurring_tot(self):
        for account in self:
            res = sum(line.montant for line in account.autre_id)
            resfact = sum(line.price_subtotal for line in account.order_line)
            
            account.total_facture = res + resfact
            account.sous_total = resfact



    def button_confirm(self):
        res= super(PurchaseOrder, self).button_confirm()
        verification = self.env['stock.picking'].search([('origin', '=', self.name)])
        if verification:
            verification.bailleur_id = self.bailleur_id.id
        return res
    



    

    
class achat_dkt(models.Model):

    _name = 'achat.dkt'
   

    name = fields.Date('Date')
    produit_id = fields.Many2one('product.product', string='Product',required=True)   
    montant = fields.Float('Montant')
    achat_id = fields.Many2one('purchase.order', string='Product')
    company_id = fields.Many2one('res.company', string='company')




class bailleur(models.Model):

    _name = 'bailleur'
   

    name = fields.Char('Name')


class Picking(models.Model):

    _inherit ="stock.picking"

    bailleur_id = fields.Many2one('bailleur','Bailleur')


    
class StockMoveLine(models.Model):
    
    _inherit = "stock.move.line"

    bailleur_id = fields.Many2one(related='picking_id.bailleur_id', store=True, string='Bailleur')
    


    

   
    


   

            
    
    
  
    
    
            
  
