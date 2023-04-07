from django.urls import path
from . import views
urlpatterns = [
    path("book_list/", views.BookList.as_view(), name="book_list"),
    path("<int:pk>/", views.BookDetail.as_view(), name="book_detail"),
    path("search/", views.Search.as_view(), name="search"),
    path("teste/", views.TesteListBook.as_view(), name="teste"),

    # own book list
    path("own_book_list/", views.OwnBookList.as_view(), name="own_book_list"),
    path("create/", views.BookCreate.as_view(), name="create_book"),
    path("delete/<int:pk>/", views.DeleteBook.as_view(), name="delete_book"),
    path("update/<int:pk>/", views.UpdateBook.as_view(), name="update_book")
]