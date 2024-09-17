from django.urls import path
from . import views

from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("", views.account, name="account"),
    path("order_history/<order_number>",
         views.order_history,
         name="order_history"
        ),
]