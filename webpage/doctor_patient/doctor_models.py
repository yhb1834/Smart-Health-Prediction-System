from django.db import models


#장고에서 제공하는 models.Model를 상속(장고 ORM을 이용하기 위함)
#장고 ORM은 SQL 쿼리문을 사용하지 않고, 장고 모델을 통해 DB 관리를 해줌
class Doctor_user(models.Model): 
    #CharField : 길이 제한, #TextFielld : 길이 제한 없음
    #verbose_name : 관리자 페이지에서 보여지는 이름
    username = models.CharField(max_length=20,verbose_name = 'username')
    password = models.CharField(max_length=20,verbose_name = 'password')
    #auto_now_ADD = Ture : 현재 시간 자동으로 사용
    registered_date = models.DateTimeField(auto_now_add=True,verbose_name='register_date') 

    class Meta: #메타 클래스를 이용하여 테이블명 지정
        db_table = 'doctor_user'
