from django.db import models
from accounts.models import CustomUserModel
from django.conf import settings
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user",
                             on_delete=models.CASCADE)
    first_name = models.CharField(max_length=244, default='')
    last_name = models.CharField(max_length=244, default='')
    phone = models.CharField(max_length=25, default='')
    city = models.CharField(max_length=45, default='')
    email = models.EmailField(max_length=244)
    image = models.ImageField(upload_to='media/uploads/profiles',
                              blank=True, null=True, default='')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-createdAt",)

    def __str__(self):
        return self.first_name

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000'+self.image.url
        return ''