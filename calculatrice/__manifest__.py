{
    "name": "Calculator",
    "version": "19.0.3.2.0",
    "category": "Tools",
    "summary": "A teaching calculator with six operations, contact links and a printable report",
    "description": """
Calculator
==========

A training module for learning Odoo development, with a real, usable feature set:

- Two numbers with 6 decimals and six operations: addition, subtraction, multiplication,
  division, modulo and GCD.
- The result is computed and stored automatically.
- Global search on number 1, number 2 or the result.
- Link each calculation to one or several contacts, with a "Calculations" smart button on contacts.
- Printable calculation report (PDF).
- User and Manager security groups.
- English and French translations.
""",
    "author": "Script Consulting",
    "maintainer": "Script Consulting",
    "website": "https://github.com/MaxTemat/Odoo-Calculatrice",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/calculatrice_views.xml",
        "views/res_partner_views.xml",
        "report/calculatrice_report.xml",
    ],
    "images": [
        "static/description/screenshot_1_list.jpg",
        "static/description/screenshot_2_form.jpg",
        "static/description/screenshot_3_partner.jpg",
    ],
    "installable": True,
    "application": True,
}
