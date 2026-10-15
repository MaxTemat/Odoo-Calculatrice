from odoo import api, fields, models
import math


class Calculatrice(models.Model):
    _name = "calculatrice.calculatrice"
    _description = "Calculator"

    # =========================================================
    # CHAMPS
    # =========================================================

    nombre1 = fields.Float(
        string="Number 1",
        digits=(16, 6),
    )

    nombre2 = fields.Float(
        string="Number 2",
        digits=(16, 6),
    )

    operation = fields.Selection(
        selection=[
            ("addition", "Addition"),
            ("soustraction", "Subtraction"),
            ("multiplication", "Multiplication"),
            ("division", "Division"),
            ("modulo", "Modulo"),
            ("pgcd", "GCD"),
        ],
        string="Operation",
        default="addition",
        required=True,
    )

    resultat = fields.Float(
        string="Result",
        digits=(16, 6),
        compute="_compute_resultat",
        store=True,
    )

    recherche = fields.Char(
        string="Number 1 or Number 2 or Result",
        compute="_compute_recherche",
        search="_search_recherche",
    )

    contact_ids = fields.Many2many(
        comodel_name="res.partner",
        string="Contacts",
    )

    # =========================================================
    # CALCUL DU RÉSULTAT
    # =========================================================

    @api.depends("nombre1", "nombre2", "operation")
    def _compute_resultat(self):
        for record in self:
            n1 = record.nombre1
            n2 = record.nombre2

            if record.operation == "addition":
                record.resultat = n1 + n2

            elif record.operation == "soustraction":
                record.resultat = n1 - n2

            elif record.operation == "multiplication":
                record.resultat = n1 * n2

            elif record.operation == "division":
                record.resultat = n1 / n2 if n2 != 0 else 0.0

            elif record.operation == "modulo":
                record.resultat = n1 % n2 if n2 != 0 else 0.0

            elif record.operation == "pgcd":
                record.resultat = math.gcd(
                    int(n1),
                    int(n2),
                )

            else:
                record.resultat = 0.0

    # =========================================================
    # RECHERCHE GLOBALE
    # =========================================================

    @api.depends("nombre1", "nombre2", "resultat")
    def _compute_recherche(self):
        for record in self:
            record.recherche = (
                f"{record.nombre1:g} "
                f"{record.nombre2:g} "
                f"{record.resultat:g}"
            )

    def _search_recherche(self, operator, value):
        if not value:
            return []

        try:
            number = float(value.replace(",", "."))
        except (ValueError, AttributeError):
            return [("id", "=", 0)]

        return [
            "|",
            "|",
            ("nombre1", operator, number),
            ("nombre2", operator, number),
            ("resultat", operator, number),
        ]

    def action_imprimer(self):
        self.ensure_one()
        report = self.env.ref(
            "calculatrice.action_report_calculatrice"
        )
        return report.report_action(self)