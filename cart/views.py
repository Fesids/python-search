from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateResponseMixin,View
from django.shortcuts import get_object_or_404, redirect
from .models import Cart
from book.models import Book

# Create your views here.

class CartListProducts(TemplateResponseMixin, View):
    model = Cart
    template_name = "cart/manage/cart_products.html"
    cart = None
    products = None

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        self.cart = get_object_or_404(Cart, cart_owner=user)
        return super().dispatch(request)

    def get(self, request, *args, **kwargs):
        '''sum = 0
        for book in self.cart.products.all():
            sum += book.price'''
        self.products = self.cart.products.all()

        sum = 0
        [sum := sum + book.price for book in self.products]

        return self.render_to_response({"products": self.products, "cart": self.cart, "sum": sum})

    '''def post(self, request, *args, **kwargs):
        self.products = self.products.all().pop(kwargs.pk)
        return redirect("own_cart")'''


class CartAddProducts(TemplateResponseMixin, View):
    model = Cart
    template_name = "cart/manage/add_product.html"
    cart = None
    products = None
    product_to_add = None

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        self.cart = get_object_or_404(Cart, cart_owner=user)
        return super().dispatch(request)

    def get(self, request,*args, **kwargs):
        pk = self.kwargs.get("pk")
        self.product_to_add = get_object_or_404(Book, id=pk)
        self.products = self.cart.products.all()

        return self.render_to_response({"products": self.products, "cart": self.cart, "product": self.product_to_add})

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        self.product_to_add = Book.objects.filter(id=pk)
        self.cart.products.add(self.product_to_add[0].id)
        return redirect("own_cart")
        # return self.render_to_response({"product": self.product_to_add})


class CartRemoveProduct(TemplateResponseMixin, View):
    model = Cart
    template_name = "cart/manage/remove_product.html"
    cart = None
    products = None
    product_to_remove = None

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        self.cart = get_object_or_404(Cart, cart_owner=user)
        return super().dispatch(request)

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        self.product_to_remove = self.cart.products.all().get(id=pk)

        return self.render_to_response({"product": self.product_to_remove})

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        self.product_to_remove = self.cart.products.all().get(id=pk)
        self.cart.products.remove(self.product_to_remove)

        return redirect("own_cart")