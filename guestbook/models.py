from django.db import models

# Create your models here.
class Guestbook(models.Model):
    no = models.AutoField(primary_key=True) # 자동증가, 기본키설정
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    content = models.TextField()  # 길이 제한 없는 문자열
    regdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Guestbook({self.no}, {self.name}, {self.password}, {self.content}, {self.regdate})'