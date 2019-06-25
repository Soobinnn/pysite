from django.db import models
from user.models import User

# Create your models here.


class Board(models.Model):
    board_no = models.AutoField(primary_key=True) # 자동증가, 기본키설정
    title = models.CharField(max_length=100)
    contents = models.TextField()  # 길이 제한 없는 문자열
    hit = models.IntegerField()
    reg_date = models.DateTimeField(auto_now=True)
    group_no = models.IntegerField(default=0)
    order_no = models.IntegerField(default=0)
    depth = models.IntegerField(default=0)
    no = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Board({self.board_no}, {self.title}, {self.contents}, {self.hit}, {self.reg_date}, {self.group_no}, {self.order_no}, {self.depth}, {self.no})'