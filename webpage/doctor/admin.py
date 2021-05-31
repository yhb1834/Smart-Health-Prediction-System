from django.contrib import admin
from .models import Doctor_user,Patient_list,Prescription,Feedback,Reservation,Earnings
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from doctor_patient.models import User

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
    list_display = (
        'doctor_name',              
        'patient_name', 
            'symptom', 
            'date'
    )
    
class Prescription_Admin(admin.ModelAdmin):
    list_display = (
        'doctor_name',              
        'patient_name', 
            'diagnosis', 
            'symptom',
            'date'
    )
    
 
class Feedback_Admin(admin.ModelAdmin):
    list_display = (
            'username',              
            'title', 
            'content',
            'date'
    )  
    
class Resevation_Admin(admin.ModelAdmin):
    list_display = (
            'doctor_name',              
            'patient_name', 
            'date',
            'time',
            'type',
            'content'
    )  

class Earnings_Admin(admin.ModelAdmin):
    list_display = (
            'doctor_name',              
            'bank', 
            'account',
            'money',
    )  
    
class User_Admin(admin.ModelAdmin):
    list_display = (
            'username',              
    )    
    
admin.site.register(Doctor_user, Doctor_user_admin)
admin.site.register(Patient_list, Patient_list_Admin)
admin.site.register(Prescription, Prescription_Admin)
admin.site.register(Feedback, Feedback_Admin)
admin.site.register(Reservation, Resevation_Admin)
admin.site.register(Earnings, Earnings_Admin)
admin.site.register(User, User_Admin)