from django.db import models

# Create your models here.
class User(models.Model):
    no = models.AutoField(primary_key=True) # 자동증가, 기본키설정
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=32)
    gender = models.CharField(max_length=10)
    joindate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'User({self.no}, {self.name}, {self.email}, {self.password}, {self.gender}, {self.joindate})'