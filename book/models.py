from django.db import models
from django.urls import reverse
from django.core.files import File
from django.conf import settings

from io import BytesIO
from PIL import Image

from accounts.models import CustomUserModel
# Create your models here.


class Booktype(models.Model):
    btype = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(default=btype)

    class Meta:
        ordering = ('btype',)

    def __str__(self):
        return self.btype


class Book(models.Model):
    author_post = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="author_post",
                                  on_delete=models.CASCADE)
    book_name = models.CharField(max_length=150)
    slug = models.SlugField(default=book_name)
    author_name = models.CharField(max_length=150)
    type = models.ForeignKey(Booktype, related_name="type",
                             on_delete=models.CASCADE)
    price = models.FloatField()
    image = models.ImageField(upload_to="media/uploads/", blank=True, null=True, default=" ")
    thumbnail = models.ImageField(upload_to="media/uploads/", blank=True, null=True, default=" ")

    class Meta():
        ordering = ('book_name',)

    def __str__(self):
        return self.book_name

    def get_url(self):
        return reverse('book_detail', args=[self.id])

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000'+self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000'+self.thumbnail.url

        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000'+self.thumbnail.url

            else:
                return ''