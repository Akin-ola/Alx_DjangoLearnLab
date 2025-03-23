from django.contrib import admin
from .models import Post, Profile

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'published_date', 'author']
    list_filter = ['published_date']
    search_fields = ['title', 'author']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']
    list_filter = ['user']
    search_fields = ['user']