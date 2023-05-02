from django.db import models
from django.conf import settings
from book.models import Book
# Create your models here.

class Cart(models.Model):
    cart_owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="cart_user",
                                   on_delete=models.CASCADE)
    products = models.ManyToManyField(Book, related_name="books_to_buy",
                                      blank=True)

