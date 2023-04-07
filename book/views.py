from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.db.models import Q
from django.shortcuts import redirect
from .models import Book, Booktype
from .forms import CreateBookForm
from django.utils.text import slugify
from django.urls import reverse, reverse_lazy
import operator
from functools import reduce

# Create your views here.

class BookGeneric(View):
    model = Book


class BookList(TemplateResponseMixin, BookGeneric):

    template_name = "search_templates/book_list.html"
    books = None

    def get(self, request, format=None):

        self.books = Book.objects.all()

        return self.render_to_response({
            "books": self.books
        })

# book detail
class BookDetail(generic.DetailView):
    model = Book
    template_name = "search_templates/book_detail.html"


class BookCreate(generic.CreateView, LoginRequiredMixin):
    model = Book
    template_name = "book/manage/create_book.html"

    def get_formset(self, data=None):
        return CreateBookForm(data=data)

    def get(self, request, format=None):
        form = self.get_formset()
        return self.render_to_response({
            "form": form
        })

    def post(self, request, *args, **kwargs):

        form = CreateBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author_post = request.user
            form.instance.slug = slugify(form.cleaned_data['book_name'])
            form.save()
            return redirect("own_book_list")
        return self.render_to_response({
            "form": form
        })


class DeleteBook(generic.DeleteView, LoginRequiredMixin):
    template_name = "book/manage/delete_book.html"
    model = Book
    context_object_name = "book"
    success_url = reverse_lazy("own_book_list")


class UpdateBook(generic.UpdateView,LoginRequiredMixin):
    model = Book
    template_name = "book/manage/update_book.html"
    fields = ["book_name", "type", "author_name", "price", "image", "thumbnail"]
    success_url = reverse_lazy("own_book_list")


# function to search book by name, author and type
class Search(TemplateResponseMixin, View):
    template_name = "search_templates/search.html"
    results = []

    def get(self, request, format=None):

        query = request.GET.get('search')
        if query == '':
            query = None


        self.results = Book.objects.filter(
            Q(book_name__icontains=query) | Q(author_name__icontains=query)
            | Q(type__btype__icontains=query)


        )

        return self.render_to_response({
            "query": query,
            "results": self.results
        })

# ownbooklist


class OwnBookList(TemplateResponseMixin, View, LoginRequiredMixin):
    template_name = "book/manage/own_book_list.html"
    own_book_list = None

    def dispatch(self, request, *args, **kwargs):
        self.own_book_list = Book.objects.filter(author_post=request.user)
        return super().dispatch(request)

    def get(self, request, format=None):
        return self.render_to_response({"book_list": self.own_book_list})







class TesteListBook(ListView):
    model = Book
    template_name = "search_templates/teste_list.html"