from django.contrib import admin
from medical.models import Patient, Medicine


# Register your models here.
#@admin.register(Patient,Medicine)
class PatientAdmin(admin.ModelAdmin):
	list_display =('id','Patient_Name', 'Address', 'City', 'Doctor', 'Phno_NO')

class MedicineAdmin(admin.ModelAdmin):
	list_display =('id', 'name','quantity', 'purchase_date', 'expiration_date')


admin.site.register(Patient,PatientAdmin)
admin.site.register(Medicine,MedicineAdmin)
