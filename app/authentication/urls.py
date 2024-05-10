from django.urls import path, include

from .jwt_views import CustomRefreshView
from .views import SignupView, LoginView


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("refresh/", CustomRefreshView.as_view(), name="refresh"),
]
