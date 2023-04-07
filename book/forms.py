from django import forms
from .models import Book


class CreateBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ["book_name", "type", "author_name", "price", "image", "thumbnail"]


class UpdateBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ["book_name", "type", "author_name", "price", "image", "thumbnail"]