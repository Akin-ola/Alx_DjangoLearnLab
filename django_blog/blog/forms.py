from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import Comment, Post, Profile
from django.core.exceptions import ValidationError


class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
    def clean(self):
        return super().clean()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
    def clean(self):
        return super().clean()
    

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
    def clean(self):
        return super().clean()
    

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
    def clean(self):
        cleaned = super().clean()
        content = cleaned.get('content')
        if len(content) > 200:
            raise ValidationError('Content cannot be more than 200.')
        return cleaned
    

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model= User
        fields= ['username', 'email', 'password1', 'password2']
    def clean(self):
        return super().clean()


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'bio', 'profile_picture']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']