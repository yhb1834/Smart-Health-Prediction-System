from django.contrib import admin
from .models import Doctor_user,Patient_list


#장고 admin 페이지에서 그룹 관리할 때 쓰는 거임 

class Doctor_user_admin(admin.ModelAdmin):
    list_display = (
        'username',
        'password',
        'registered_date',
        'email'
    )
    
#@admin.register(Patient_list)
class Patient_list_Admin(admin.ModelAdmin):
    list_display = ('doctor_name', 
                    'patient_name', 
                    'symptom', 
                    'date')
    
admin.site.register(Doctor_user, Doctor_user_admin)
admin.site.register(Patient_list, Patient_list_Admin)