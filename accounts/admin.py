from django.contrib import admin
from .models import CustomUserModel
from .forms import CustomUserChangeForm, CustomUserCreationForm
# Register your models here.

@admin.register(CustomUserModel)
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUserModel
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ['email', 'username', 'is_active', 'is_staff', 'is_superuser']
    search_fields = ['email', 'username']
