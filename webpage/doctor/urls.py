from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'doctor'

urlpatterns = [
        #doctor urls
    path('main/', views.doctor_main),
    path('login/',  views.doctor_login),
    path('signup/', views.doctor_signup),
    path('logout/', views.doctor_logout),
    path('patient-list/', views.doctor_patient_list),
    path('prescription/', views.doctor_prescription),
    path('reservation/', views.doctor_reservation),
    path('feedback/', views.doctor_feedback),
    path('earnings/',views.doctor_earnings)
]