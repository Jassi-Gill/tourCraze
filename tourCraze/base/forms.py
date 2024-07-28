from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import CusUser

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = CusUser
        fields = ["name", "username",  "email", "password1", "password2"]

class UpdateUser(ModelForm): 
    class Meta:
        model = CusUser
        fields  = ["name", "avatar", "username",  "email", "bio"]
