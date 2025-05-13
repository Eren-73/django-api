from django.contrib import admin
from django.urls import path

from devise import views

urlpatterns = [
  path("" , views.dashboard, name = "index"),
  path("days=<int:days_range>&currencies=<str:currencies>/", views.dashboard, name="index"),]