from django.db import models

class Person(models.Model):
    user_name = models.CharField(max_length=50,null=False , verbose_name="ЛОГИН")
    password = models.CharField(max_length=100 , null=False , verbose_name="ПАРОЛЬ")
