from . import views
from django.urls import path

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('amend/<item_id>/', views.amend_cart, name='amend_cart'),
    path('remove/<item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
