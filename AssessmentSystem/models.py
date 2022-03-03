from django.db import models
from django.conf import settings
# Create your models here.


class Users(models.Model):  
    middle_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=13)
    profile = models.ImageField()
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Income(models.Model):
    income_id = models.AutoField(primary_key=True)
    income_amount = models.IntegerField()
    plan_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Plan(models.Model):
    plan_id  = models.AutoField(primary_key=True)
    plan_details = models.CharField(max_length=200, default='0')
    plan_amount = models.IntegerField()
    plan_name= models.CharField(max_length=200, default='0')
    # plans = models.CharField(income, on_delete=models.CASCADE)


class Expenses(models.Model):
    expenses_id = models.AutoField(primary_key=True)
    expenses_name = models.CharField(max_length=200, default='0')
    expenses_amount = models.IntegerField()
    plan_id = models.ForeignKey(Plan, on_delete=models.CASCADE)
