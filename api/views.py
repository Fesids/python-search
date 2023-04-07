from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from .serializer import BookSerializers, BooktypeSerializer, ProfileSerializer, CustomUserSerializer
from rest_framework import views
from django.utils.text import slugify
from book.models import Book, Booktype
from profiles.models import Profile
from accounts.models import CustomUserModel
# Create your views here.


'''
    
    /* Book API Setup *

'''


class BookMixin:
    permission_classes = (AllowAny,)
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class BookListApi(BookMixin,generics.ListAPIView):
    pass


class BookDetail(BookMixin, generics.RetrieveUpdateDestroyAPIView):
   pass


class BookCreateApi(BookMixin, views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response({"status": "success", "book": serializer.data}, status.HTTP_201_CREATED)

        else:
            return Response({"status": "fail", "message": serializer.errors}, status.HTTP_400_BAD_REQUEST)


class BookDelete(BookMixin, views.APIView):
    permission_classes = [AllowAny, ]

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        self.book = get_object_or_404(Book, id=id)

        if not self.book:
            return Response({"message": f"book with id {id} not found"}, status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(instance=self.book)

        return Response({"book": serializer.data})

    def delete(self, request, *args, **kwargs):
        id= kwargs.get("id")
        book = get_object_or_404(Book, id=id)

        if(book):
            try:

                book.delete()

                return Response({"message": "deleted"}, status.HTTP_204_NO_CONTENT)


            except:
                return Response({"status": "something went wrong in deleting post"}, status.HTTP_400_BAD_REQUEST)

        else:
            return Response({"status": f"book with id {id} don't exist"}, status.HTTP_400_BAD_REQUEST)


class BookUpdate(BookMixin, views.APIView):
    permission_classes = [AllowAny,]
    book = None

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        self.book = get_object_or_404(Book, id=id)

        if not self.book:
            return Response({"message": f"book with id {id} not found"}, status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(instance=self.book)

        return Response({"book": serializer.data})

    def put(self, request, *args, **kwargs):
        id = kwargs.get("id")
        self.book = get_object_or_404(Book, id=id)

        if not self.book:
            return Response({"message": f"book with id {id} not found"}, status.HTTP_400_BAD_REQUEST)

        data = {

            # "author_post": request.data.get("author_post"),

            "book_name" : request.data.get("book_name"),
            "slug" : request.data.get("slug"),
            "author_name" : request.data.get("author_name"),
            "type" : request.data.get("type"),
            "price" : request.data.get("price"),
            "image" : request.data.get("image"),
            "thumbnail" : request.data.get("thumbnail")

        }

        serializer = self.serializer_class(instance=self.book, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({"body": serializer.data}, status.HTTP_200_OK)
        return Response({"message": serializer.errors}, status.HTTP_400_BAD_REQUEST)


'''

    /* Profiles API Setup *

'''


class ProfileMixin:
    permission_classes = (AllowAny,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileListApi(ProfileMixin, generics.ListAPIView):
    pass


class ProfileDetail(ProfileMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


'''
    /* Customuser API setup
'''


class CustomUserMixin:
    permission_classes = (AllowAny,)
    queryset = CustomUserModel.objects.all()
    serializer_class = CustomUserSerializer


class UserListApi(CustomUserMixin, generics.ListAPIView):
    pass


class UserDetailApi(CustomUserMixin, generics.RetrieveUpdateDestroyAPIView):
    pass

'''

    /* Profiles API Booktype *

'''


class BooktypeMixin:
    permission_classes = (AllowAny,)
    queryset = Booktype.objects.all()
    serializer_class = BooktypeSerializer


class BooktypeList(BooktypeMixin, generics.ListAPIView):
    pass


class BooktypeDetail(BooktypeMixin, generics.RetrieveUpdateDestroyAPIView):
    pass
