from django.urls import path
from .views import (
    LoginView, 
    RegisterView,
    LogoutUserView
    )


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('logout/', LogoutUserView.as_view(), name="logout"),
]