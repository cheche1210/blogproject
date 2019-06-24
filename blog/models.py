from django.db import models

class Blog(models.Model):#어떤변수의 어떤 타입의 데이터
   title = models.CharField(max_length=200)
   pub_date = models.DateTimeField('date published')
   body = models.TextField()#조금 더 긴 문장

   def __str__(self):
       return self.title #글 목록 제목으로 보여지기

   def summary(self):
       return self.body


   



# Create your models here.
