from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit=['mail.thread','mail.activity.mixin']
    _description = 'Hospital Appointment'
    _rec_name='ref'

    patient_id=fields.Many2one('hospital.patient',string="Patient")
    gender = fields.Selection(related="patient_id.gender")
    appointment_time=fields.Datetime('Appointment Date', default=fields.Datetime.now)
    reserved_date=fields.Date('Reserve', default=fields.Date.context_today)
    ref = fields.Char(string='Reference')
    html_template= fields.Html(string="Html Code")
    priority=fields.Selection([
        ('0','Normal'),
        ('2', 'Low'),
        ('3', 'High'),
        ('4', 'Very High'),
    ], string="Priority", help="give the priority patient")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Canceled'),
    ], string="State", default="draft", required=True)

    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        self.ref=self.patient_id.ref

    def action_test(self):
        print('Hello Button')
        return{
            'effect':{
                'fadeout':'slow',
                'message':'Success clicked',
                'type':'rainbow_man'
            }
        }