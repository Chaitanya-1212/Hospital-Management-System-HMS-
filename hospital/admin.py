from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(DoctorModel)
admin.site.register(PatientModel)
admin.site.register(AppointmentModel)
admin.site.register(ProfileModel)
admin.site.register(Appointment_done_Model)

