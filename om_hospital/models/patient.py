from datetime import date

from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit=['mail.thread','mail.activity.mixin']
    _description = 'Hospital Patient'
    _rec_name = 'ref'

    # id= fields.Integer(string='ID Custom', required=True)
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
        vals['ref']=self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)

    def write(self, vals):
        if not self.ref and not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient,self).write(vals)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today=date.today()
            if rec.date_of_birth:
                rec.age=today.year-rec.date_of_birth.year
            else:
                rec.age=0

# xpath

