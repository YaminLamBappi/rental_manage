from django.urls import path
from .views import signup_view, login_view, logout_view, profile_view, edit_profile_view

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_view, name="profile"),
    path("edit_profile/", edit_profile_view, name="edit_profile"),
]
