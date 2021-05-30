from django.db import models
from django.contrib.auth.models import User
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from doctor_patient.models import User

#장고에서 제공하는 models.Model를 상속(장고 ORM을 이용하기 위함)
#장고 ORM은 SQL 쿼리문을 사용하지 않고, 장고 모델을 통해 DB 관리를 해줌
class Doctor_user(models.Model): 
    #CharField : 길이 제한, #TextFielld : 길이 제한 없음
    #verbose_name : 관리자 페이지에서 보여지는 이름
    #user_id = models.CharField(max_length=20,verbose_name = 'userid')
    username = models.CharField(max_length=20,verbose_name = 'username',blank=True)
    password = models.CharField(max_length=20,verbose_name = 'password')
    #auto_now_ADD = Ture : 현재 시간 자동으로 사용
    registered_date = models.DateTimeField(auto_now_add=True,verbose_name='register_date') 
    email = models.EmailField(max_length=50,unique=True,verbose_name = 'email')
    money = models.IntegerField(verbose_name='money',unique = False,default=0)
    
    def __str__(self):
        return self.username
    
    class Meta: #메타 클래스를 이용하여 테이블명 지정
        db_table = 'doctor_user'
        verbose_name = 'doctor_user'
        verbose_name_plural = 'doctor_user'
      
#환자 대기목록 
class Patient_list(models.Model):
    doctor_name = models.ForeignKey('doctor.doctor_user', on_delete=models.CASCADE, verbose_name="doctor_name")
    #patient_name = models.ForeignKey('doctor_patient.User', on_delete=models.CASCADE, verbose_name="patient")
    patient_name = models.CharField(max_length=20, verbose_name="patient",blank=True)
    symptom  = models.TextField(verbose_name="symptom",blank=True)
    date = models.DateTimeField(verbose_name="date",blank=True)

    def __str__(self):
        return str(self.doctor_name)

    class Meta:
        db_table            = 'patient_list'
        verbose_name        = 'patient list'
        verbose_name_plural = 'patient list'

#처방전
class Prescription(models.Model):
    doctor_name = models.ForeignKey('doctor.doctor_user', on_delete=models.CASCADE, verbose_name="doctor_name")
    patient_name = models.CharField(max_length=20, verbose_name="patient",blank=True)
    diagnosis  = models.TextField(verbose_name="symptom",blank=True)
    symptom  = models.TextField(verbose_name="symptom",blank=True)
    date = models.DateTimeField(auto_now_add=True,verbose_name='date') 

    def __str__(self):
        return str(self.doctor_name)

    class Meta:
        db_table            = 'prescription'
        verbose_name        = 'prescription'
        verbose_name_plural = 'prescription'