from odoo import models, fields


class DeliveryModel(models.Model):
    _name = 'delivery.options'
    _description = 'Delivery options model'
    
   
    
    delivery_timing = fields.Selection(
        [ ('asap','ASAP'),  ('move','Verhuis'), ('contruction','Nieuwbouw'), ('client_choise','Latere datum')],
        string="Levering vanaf",
        required=True
        
    )

    delivery_timing_date = fields.Date(string="Levering mogelijk vanaf")

    delivery_location = fields.Selection(
         [('house', 'Huis'), ('apartment', 'Appartement')],
        string="Type woning"
    )

    delivery_floor = fields.Integer(string="Verdieping")

    delivery_floor_elevator = fields.Boolean(string="Lift beschikbaar")

    delivery_elevator_width = fields.Integer(string="Breedte lift")

    delivery_elevator_depth = fields.Integer(string="Diepte lift")

    delivery_elevator_height = fields.Integer(string="Hoogte lift")

    delivery_staircase_type = fields.Selection(
         [('straight', 'Rechte trap'), ('corner', 'Rechte trap met een knik'), ('spiral', 'Wenteltrap')],
        string="Type trap"
    )

    delivery_staircase_width = fields.Integer(string="Breedte trap")


 
