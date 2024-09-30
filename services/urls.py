from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_services, name='services'),
    path('<service_id>', views.service_page, name='service_page'),
]
