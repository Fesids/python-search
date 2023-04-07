from django.contrib import admin
from .models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ['first_name', 'last_name', 'phone', 'city', 'email']
    search_fields = ['first_name','last_name']
