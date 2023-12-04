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
    html_template= fields.Html()
    priority=fields.Selection([
        ('0','Normal'),
        ('2', 'Low'),
        ('3', 'High'),
        ('4', 'Very High'),
    ], string="Priority", help="give the priority patient")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'Processing'),
        ('done', 'Done'),
        ('cancel', 'Canceled'),
    ], string="State", default="draft", required=True)
    doctor_id=fields.Many2one('res.users', string='Docktor', tracking=True)
    pharmacy_line_ids=fields.One2many('appointment.pharmacy.lines','appointment_id',string='Pharmacy Lines')
    hide_sales_price=fields.Boolean('Hide Sales Price')


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

    def action_in_consultation(self):
        for rec in self:
            rec.state='in_consultation'
        # print('hello')

    def action_done(self):
        for rec in self:
            rec.state='done'
        # print('hello')

    def action_cancel(self):
        for rec in self:
            rec.state='cancel'
        # print('hello')

    def action_draft(self):
        for rec in self:
            rec.state='draft'

class AppointmentPharmacyLines(models.Model):
    _name="appointment.pharmacy.lines"
    _description="Appointment Pharmacy Lines"

    product_id= fields.Many2one('product.product', required=True)
    price_unit = fields.Float(related='product_id.list_price')
    qty= fields.Integer(string='Quantity',default=1)
    appointment_id=fields.Many2one('hospital.appointment',string='Appointment')

