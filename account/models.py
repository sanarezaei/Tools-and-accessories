from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

from datetime import timedelta

import random

class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, verbose_name='نام کاربری')
    phone_number = models.CharField(max_length=15, unique=True,\
        verbose_name='تلفن')
    email = models.EmailField(null=True, blank=True, verbose_name='ایمیل')
 
    def __str__(self):
        return self.username
    
 
class OTPManager(models.Manager):
    def create_otp(self, phone_number):
        otp_code = str(random.randint(10000, 99999))  
        otp_instance = self.create(phone_number=phone_number, code=otp_code)
        return otp_instance
    
    def validate_otp(self, phone_number, otp_code):
        try: 
            otp_instance = self.get(phone_number=phone_number, code=otp_code)
            if otp_instance.is_valid():
                return True
            return False
        except OTP.DoesNotExist:
            return False
 
    
class OTP(models.Model):
    phone_number = models.CharField(max_length=15, unique=True,\
        verbose_name='شماره تلفن')
    code = models.CharField(max_length=5, verbose_name='کد ورود')
    created_at = models.DateTimeField(auto_now_add=True)
    object = OTPManager()
    
    def is_valid(self):
        validity_period = timedelta(minutes=4)
        return now() <= created_at + validity_period 
    
    def __str__(self):
        return f"{self.phone_number} : {self.code}"
    
        
class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,\
        related_name='custom_user')
    first_name = models.CharField(max_length=255, verbose_name='نام')
    last_name = models.CharField(max_length=255, verbose_name='نام خانوادگی')
    province = models.CharField(max_length=255, verbose_name='استان')
    city = models.CharField(max_length=255, verbose_name='شهر')
    address = models.TextField(verbose_name='آدرس')
    postal_code = models.IntegerField(verbose_name='کد پستی')
    
    def __str__(self):
        return f"{sef.user}: {self.province} - {self.city}"
    