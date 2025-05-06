from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('members/categories.html', views.members, name='memers'),  
]