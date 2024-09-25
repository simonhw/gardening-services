from . import views
from django.urls import path

urlpatterns = [
    path('', views.contact_us, name='contact_us'),
    path('subscribe/', views.subscribe_page, name='subscribe'),
]