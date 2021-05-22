from django.urls import path
from . import doctor_views   


urlpatterns = [
   path('signup/',doctor_views.doctor_signup),  
   #즉, 최종적인 url은 127~~~~:8000/user/register가 된다.
] 



    #path('doctor/main/', doctor_views.doctor_main),
    #path('doctor/login/', doctor_views.doctor_login),
    #path('doctor/signup/', doctor_views.doctor_signup),

    
    # doctor urls

    
    # path('doctor/main',views.doctor_main,name='doctor_main'),
    # path('doctor/signup', views.doctor_signup,name='doctor_signup'),
    # path('doctor/login', views.doctor_login,name='doctor_login'),
    # path('doctor/patient_list',views.doctor_patient_list,name='doctor_patient_list'),
    # path('doctor/prescription',views.doctor_prescription,name='doctor_prescription'),
    # path('doctor/feedback', views.doctor_feedback,name='doctor_feedback'),
    # path('doctor/reservation', views.doctor_reservation,name='doctor_reservation'),
    # path('doctor/medical_expense',views.doctor_medical_expense,name='doctor_medical_expense'),