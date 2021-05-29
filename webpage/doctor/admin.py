from django.contrib import admin
from .models import Doctor_user


#장고 admin 페이지에서 그룹 관리할 때 쓰는 거임 
@admin.register(Doctor_user)
class Doctor_user_admin(admin.ModelAdmin):
    list_display = (
        'username',
        'password',
        'registered_date',
        'email'
    )