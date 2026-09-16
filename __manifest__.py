{
    "name": "Calculatrice",
    "version": "1.1",
    "category": "Tools",
    "summary": "Calculatrice pédagogique avec deux nombres",
    "description": "Module de formation Python/Odoo avec deux champs Float à 6 décimales.",
    "author": "Max Temat",
    'website': 'https://github.com/MaxTemat?tab=repositories',
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/calculatrice_views.xml",
        "views/res_partner_views.xml"
    ],
    "installable": True,
    "application": True
}
