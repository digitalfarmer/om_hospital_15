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

    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        self.ref=self.patient_id.ref