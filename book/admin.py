from django.contrib import admin
from .models import Booktype, Book
# Register your models here.

@admin.register(Booktype)
class BookTypeAdmin(admin.ModelAdmin):
    list_filter = ["btype"]
    list_display = ['btype']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ["book_name", "type"]
    list_filter = ["type"]
    list_display = ["book_name","author_name","type","price"]
