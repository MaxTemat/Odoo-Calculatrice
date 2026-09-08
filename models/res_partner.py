from odoo import _, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    calcul_count = fields.Integer(
        string="Calculs",
        compute="_compute_calcul_count",
    )

    def _compute_calcul_count(self):
        for partner in self:
            partner.calcul_count = self.env[
                "calculatrice.calculatrice"
            ].search_count([
                ("contact_ids", "in", partner.id),
            ])

    def action_view_calculs(self):
        self.ensure_one()

        return {
            "type": "ir.actions.act_window",
            "name": _("Calculs"),
            "res_model": "calculatrice.calculatrice",
            "view_mode": "list,form",
            "domain": [
                ("contact_ids", "in", self.id),
            ],
            "context": {
                "default_contact_ids": [(6, 0, [self.id])],
            },
        }