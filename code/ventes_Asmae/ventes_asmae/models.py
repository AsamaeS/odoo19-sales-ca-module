from odoo import models, fields, api
class Ventes(models.Model):
    _name = 'soujaa.ventes'
    _description = 'CA'
    name = fields.Many2one('res.partner', string='Client')
    date_facture = fields.Date(string='Date de la demande', default=fields.Date.today)
    montant = fields.Float(string='Montant de la vente')
    chiffredaffaire = fields.Float(
        string='CA',
        compute='_compute_ca',
        store=False
    )

    @api.depends('montant')
    def _compute_ca(self):
        total = sum(self.env['soujaa.ventes'].search([]).mapped('montant'))
        for rec in self:
            rec.chiffredaffaire = total