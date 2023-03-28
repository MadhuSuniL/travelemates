from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as t


class TravelerManeger(BaseUserManager):
    
    def create_user(self,email,password,**extra):
        
        if not email:
            raise ValueError(t('Email must be required!'))
        email = self.normalize_email(email)
        user = self.model(email=email,**extra)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(trans('Superuser must have is_staff is True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(trans('Superuser must have is_superuser is True'))
        return self.create_user(email, password,**extra_fields)
    