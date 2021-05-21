"""doctor_patient URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views, patient_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ad/main/', views.ad_main),
    path('ad/login/', views.ad_login),
    path('ad/signup/', views.ad_signup),

    path('doctor/main/', views.doctor_main),
    path('doctor/login/', views.doctor_login),
    path('doctor/signup/', views.doctor_signup),

    path('patient/main', patient_views.pa_main),
    path('patient/login/', patient_views.pa_login),
    path('patient/signup/', patient_views.pa_signup),

    # admin urls
    #path('admin/main', views.admin_main, name='admin_main'), # admin 메인 페이지
    #path('admin/signup', views.admin_signup, name='admin_signup'), # admin 회원가입
    #path('admin/login', views.admin_login, name='admin_login'), # admin 로그인
    #path('admin/doctor-certify', views.admin_doctor_certify, name='admin_doctor_certify'), # admin 의사 인증
    #path('admin/disease', views.admin_disease, name='admin_disease'), # admin 질병 DB 관리
    #path('admin/feedback', views.admin_feedback, name='admin_feedback'), # admin feedback
    #path('admin/doctor-profile', views.admin_doctor_profile, name='admin_doctor_profile'), # admin 의사 프로필 DB 관리
    #path('admin/patient-profile', views.admin_patient_profile, name='admin_patient_profile'), # admin 환자 프로필 DB 관리

    # doctor urls

    # patient urls

]
