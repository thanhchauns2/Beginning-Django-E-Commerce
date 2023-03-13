from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="catalog_home"),
    path('category/<slug:slug>/', views.show_category, name='catalog_category'),
    path('product/<slug:slug>/', views.show_product, name='catalog_product'),
] 