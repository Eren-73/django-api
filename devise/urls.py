from django.contrib import admin
from django.urls import path

from devise import views

urlpatterns = [
  path("" , views.dashboard, name = "index")
]