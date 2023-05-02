
from django.dispatch import receiver
from django.db.models.signals import post_save
from profiles.models import Profile
from .models import CustomUserModel
from cart.models import Cart
user = CustomUserModel


@receiver(post_save, sender=user)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = CustomUserModel.objects.last()
        Profile.objects.create(user=instance, first_name=user.username, last_name='', phone='9999-9999', city='unknown', email=user.email, image=' ')

@receiver(post_save, sender=user)
def create_cart(sender, instance, created, **kwargs):
    if created:
        user = CustomUserModel.objects.last()
        Cart.objects.create(cart_owner=instance)
