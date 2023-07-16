{
    "name": "Delivery",  # The name that will appear in the App list
    "version": "1.0",  # Version
    "application": True,  # This line says the module is an App, and not a module
    "category": "Sales",
    "website": "https://www.samuel-lino-finnegan-portfolio.com/",
    "description": "This module allows you to add a variety of delivery options to your Odoo store. You can choose from different carriers, shipping methods, and delivery times.",
    "summary": "Here you can find a list of options you can add to your delivery",
    "depends": ["base"],  # dependencies
    "data": [
        "security/ir.model.access.csv",
        "views/views.xml"
    ],
    "assets": {
        "web.assets_frontend": [
            "delivery_options/static/src/js/delivery_options.js"
        ]
    },
    "installable": True,
    "license": "LGPL-3",
}

