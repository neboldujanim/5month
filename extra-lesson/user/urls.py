from django.urls import path
from .views import RegistrationView, Confirm, LoginView

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('confirm/', Confirm.as_view()),
    path('login/', LoginView.as_view()),
]