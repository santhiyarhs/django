from django.db import models

# Create your models here.
class Datas(models.Model):
    Name=models.CharField(max_length=20,default=" ")
    Age=models.IntegerField(max_length=20,default=" ")
    Address=models.CharField(max_length=20,default=" ")
    Contact=models.IntegerField(max_length=20,default=" ")
    Mail=models.CharField(max_length=20,default=" ")
    

