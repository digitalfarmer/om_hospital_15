from odoo import api, fields, models


class PatientTag(models.Model):
    _name="patient.tag"
    _description="Patient Tag"

    name=fields.Char(name="name", required=True)
    active=fields.Boolean(string="Active", default=True)
    color=fields.Integer(string='Color')
    color_2=fields.Char(string='Color 2')

