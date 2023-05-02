from django.urls import path
from . import views

urlpatterns = [
    path("own_cart/", views.CartListProducts.as_view(), name="own_cart"),
    path("add_product_cart/<int:pk>/", views.CartAddProducts.as_view(), name="add_product"),
    path("own_cart/remove_from_cart/<int:pk>/", views.CartRemoveProduct.as_view(),
         name="remove_from_cart")
]