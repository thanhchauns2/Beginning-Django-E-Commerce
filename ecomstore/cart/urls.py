from django.urls import path

from . import views

urlpatterns = [
    path("cart/", views.show_cart, name="show_cart"),
] 