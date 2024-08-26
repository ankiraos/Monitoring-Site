from django.urls import path, include
from django.views.generic import (
    TemplateView,
)  # useful in displaying index.html template
from .views import (
    add_site,
    login_view,
    register_view,
    logout_view,
    home_view,
)


urlpatterns = [
    # path("login", login_view, name="login_page"),
    path("add", add_site, name="add_site_page"),
    path("register", register_view, name="register_page"),
    # path("logout", logout_view, name="logout_page"),
    path("", home_view, name="home_page"),
    path("accounts/", include("allauth.urls")),
    # path("logout", LogoutView.as_view(), name="logout"),
]
