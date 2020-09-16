from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("contact", views.contact, name="contact"),
    path("logout", views.logout, name="logout"),
    path("eventpage/<str:id>", views.eventpage, name="eventpage")
]