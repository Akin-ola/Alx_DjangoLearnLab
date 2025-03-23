from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post

class UpdateViewForm(forms.ModelForm):
    update_date = forms.DateField()
    class Meta:
        model = Post
        fields = ['title', 'content', 'update_date']

class CreateViewForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published_date', 'author']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    class Meta:
        model= User
        fields= ('username', 'email', 'password1', 'password2')


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
          'username',
          'email',
          )

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
          'bio',
          'profile_picture',
        )