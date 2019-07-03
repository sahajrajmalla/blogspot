from django.shortcuts import path
from . import views

urlpatterns = [
    path("", views.register, name="users-register"),

]
