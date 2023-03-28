from django.contrib import admin
from .models import Traveler
from django.contrib.auth.admin import UserAdmin
from .forms import TravChangeForm, TravCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as t


class TravelerAdmin(UserAdmin):
    add_form = TravCreationForm
    form = TravChangeForm
    
    model = Traveler
    list_display = ['email','name','premium','otp_verifyed','is_staff']
    list_filter = ['email','name','premium','otp_verifyed','is_staff','is_active']
    fieldsets = (
        (None,{'fields':('email','password')}),
        (t("Personal info"), {"fields": (
            'name',
            'profile'
        )}),
        ('Permissions',{'fields':('premium','otp_verifyed','is_staff','is_active')}),
        (t("Important dates"), {"fields": ("last_login", "date_joined")}),
        
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

    
admin.site.register(Traveler,TravelerAdmin)