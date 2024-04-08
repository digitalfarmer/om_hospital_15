from odoo import api, fields, models
import datetime

class CancelAppointmentWizard(models.TransientModel):
    _name="cancel.appointment.wizard"
    _description="Cancel Appointment Wizard"

    #default_get function
    @api.model
    def default_get(self, fields):
        res=super(CancelAppointmentWizard, self).default_get(fields)
        # active_id=self.env.context.get('active_id')
        res['date_cancel']= datetime.date.today()
        # appointment=self.env['hospital.appointment'].browse(active_id)
        # res.update({'appointment_id':active_id})
        return res

    appointment_id=fields.Many2one('hospital.appointment', string='Appointment')
    reason=fields.Text(string="Reason")
    date_cancel=fields.Date(string="Date Cancel")

    def action_cancel_appointment(self):
        pass;

