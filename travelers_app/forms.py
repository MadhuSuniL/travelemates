from django.contrib.auth.forms import UserChangeForm , UserCreationForm
from .models import Traveler


class TravCreationForm(UserCreationForm):
    class Meta:
        model = Traveler
        fields = ("email",)
        
        

class TravChangeForm(UserChangeForm):
    class Meta:
        model = Traveler
        fields = '__all__'

        