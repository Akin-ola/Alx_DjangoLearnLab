from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . import models


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = models.CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        return super().clean()

        
        

# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = models.CustomUser
#         fields =