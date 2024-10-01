from . import views
from django.urls import path

urlpatterns = [
    path('', views.index_page, name='home'),
    path('500-test/', views.test_500_error_page, name="500_test")
]
