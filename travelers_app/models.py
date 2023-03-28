from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as t
from .manager import TravelerManeger
from .profile_creation import create_profile_pic

class Traveler(AbstractUser, PermissionsMixin):
    
    username = None
    first_name = None
    last_name = None
    
    
    email = models.EmailField(t('email address'),unique=True)
    profile = models.ImageField(upload_to='profiles/', blank=True, null=True)
    name = models.CharField(max_length=40)
    mother_tounge = models.CharField(max_length=50,default='Telugu')
    phone_number = models.CharField(max_length=10)
    premium = models.BooleanField(default=False)
    otp_verifyed = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = TravelerManeger()
    
    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if not self.profile:
            self.profile = create_profile_pic(self.email)
        super().save(*args, **kwargs)








# class TravelerDetails(models.Model):
#     traveler = models.ForeignKey(User, on_delete=models.CASCADE)
#     profile = models.ImageField(upload_to='profiles', blank=True, null=True)
#     phone_number = models.CharField(max_length=20)
#     premium = models.BooleanField(default=False)
#     otp_verifyed = models.BooleanField(default=False)


#     def save(self, *args, **kwargs):
#         if not self.profile_pic:
#             self.profile_pic = create_profile_pic(self.traveler.username)

#         super().save(*args, **kwargs)
    