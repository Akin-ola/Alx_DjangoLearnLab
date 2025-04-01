from django.shortcuts import render, redirect
from . import forms
from django.urls import reverse_lazy
from rest_framework import generics
from .serializers import CustomUserSerializer
from .models import CustomUser
# Create your views here.


class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

# def register(request):
#     if request.method == 'POST':
#         form = forms.CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse_lazy('...'))
#     form = forms.CustomUserCreationForm()
#     return render(request, 'register.html', {'form': form})


