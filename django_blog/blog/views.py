from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate, login
from .models import Profile
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
# Create your views here.

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    class Meta:
        model= User
        fields= ('username', 'email', 'password1', 'password2')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login_view')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form })


class ProfileView(DetailView):
    model = Profile
    
@login_required(login_url='login_view')
def profile_view(request):
    if request.method == 'POST':
        ...
    return render(request, 'blog/profile.html')

    
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

@login_required(login_url='login_view')
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        form1 = UpdateProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid or form1.is_valid:
            form.save()
            form1.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
        form1 = UpdateProfileForm(instance=request.user.profile)
        forms = {
          'form': form,
          'form1': form1,
          }
        return render(request, 'blog/profile_edit.html', forms)