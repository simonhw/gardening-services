from . import views
from django.urls import path

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
]