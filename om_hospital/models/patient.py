from datetime import date

from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit=['mail.thread','mail.activity.mixin']
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date('Date of Birth')
    ref = fields.Char(string='Reference')
    age= fields.Integer(string='Age', compute="_compute_age", tracking=True)
    gender= fields.Selection([('male','Male'),('female','Female')], string='Gender',tracking=True)
    active=fields.Boolean(string="Active", default=True)
    appointment_id=fields.Many2one('hospital.appointment',string="Appointments")
    image=fields.Image(string="image")
    tag_ids=fields.Many2many('patient.tag', string='Tags')

    @api.model
    def create(self, vals):
        print("create patient")
        vals['ref']='OMTEST'
        return super(HospitalPatient, self).create(vals)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today=date.today()
            if rec.date_of_birth:
                rec.age=today.year-rec.date_of_birth.year
            else:
                rec.age=0