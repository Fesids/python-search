from django.urls import path
from . import views
urlpatterns =[

     #   /* Book api path

    path("book_list/", views.BookListApi.as_view(), name="book_list_api"),
    path("book_list/book_detail/<int:pk>/", views.BookDetail.as_view(), name="book_detail_api"),
    path("book_list/book_create/", views.BookCreateApi.as_view(), name="book_create_api"),
    path("book_list/book_update/<int:id>/", views.BookUpdate.as_view(), name="book_update_api"),
    path("book_list/book_delete/<int:id>/", views.BookDelete.as_view(), name="book_delete_api"),

    #  /* User api path

    path("user_list/", views.UserListApi.as_view(), name="user_list_api"),
    path("user_list/user_detail/<int:pk>/", views.UserDetailApi.as_view(), name="user_detail_api"),

    #  /* Booktype api path

    path("booktype_list/", views.BooktypeList.as_view(), name="booktype_list_api"),
    path("booktype_list/booktype_detail/<int:pk>/", views.BooktypeDetail.as_view(), name="booktype_detail"),

    #  /* Profile api path

    path("profile_list/", views.ProfileListApi.as_view(), name="profile_list_api"),
    path("profile_list/profile_detail/<int:pk>/", views.ProfileDetail.as_view(), name="profile_detail_api")



]