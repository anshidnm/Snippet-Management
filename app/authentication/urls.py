from django.urls import path, include

from .views import SignupView, LoginView


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignupView.as_view(), name="signup"),
]
