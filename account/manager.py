from django.db import models
from django.contrib.auth.models import BaseUserManager

import random

class CustomUserManager(BaseUserManager):
    def create_user(self, username, phone_number, password=None,\
        code=None, **extra_fields):
        if not username:
            raise ValueError("The username field is required.")
        if not phone_number:
            raise ValueError("The phone number is required")
        
        user = self.model(username=username, phone_number=phone_number,\
            code=code, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self, username, phone_number, password=None,\
        code=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(username, phone_number, password,\
            **extra_fields)
        
        

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
 
   