from django.contrib import admin
from .models import Book, CustomUser

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "publication_year"]
    list_filter = ["title", "author"]
    search_fields = ['title', 'author']

class CustomUserAdmin(admin.ModelAdmin):
    list_display= ["username", "email", "date_of_birth", "profile_photo"]

admin.site.register(Book, BookAdmin, CustomUser, CustomUserAdmin)