from book.models import Book, Booktype
from profiles.models import Profile
from accounts.models import CustomUserModel
from rest_framework import serializers

class BookSerializers(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class BooktypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booktype
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUserModel
        fields = '__all__'
