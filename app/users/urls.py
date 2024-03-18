from django.urls import path
from . import views



urlpatterns = [
    path("", views.Users.as_view()), # api/v1/users
    path("myinfo", views.MyInfo.as_view()),
    # Autentication
    path("login", views.Login.as_view()),  # django session login
    path("logout", views.Logout.as_view()), # django session logout
]
