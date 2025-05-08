from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('categories/', views.category_page, name='category_page'),
    path('sale/', views.sale_page, name='sale_page'),
    path('cart/', views.cart_page, name='cart_page'),
    path('about/', views.about_page, name='about_page'),
]