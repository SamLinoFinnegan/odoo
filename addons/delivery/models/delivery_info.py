from odoo import models, fields


class DeliveryModel(models.Model):
    _name = 'delivery.model'
    _description = 'Delivery Model'

    delivery_timing = fields.Selection(
        [ 'ASAP',  'Verhuis', 'Nieuwbouw', 'Latere datum'],
        string="Levering vanaf",
        required=True
    )

    delivery_timing_date = fields.Date("Levering mogelijk vanaf")

    delivery_location = fields.Selection(
        [('house', 'Huis'), ('apartment', 'Appartement')],
        string="Type woning"
    )

    delivery_floor = fields.Integer("Verdieping")

    delivery_floor_elevator = fields.Boolean("Lift beschikbaar")

    delivery_elevator_width = fields.Integer("Breedte lift")

    delivery_elevator_depth = fields.Integer("Diepte lift")

    delivery_elevator_height = fields.Integer("Hoogte lift")

    delivery_staircase_type = fields.Selection(
        [('straight', 'Rechte trap'), ('corner', 'Rechte trap met een knik'), ('spiral', 'Wenteltrap')],
        string="Type trap"
    )

    delivery_staircase_width = fields.Integer("Breedte trap")



