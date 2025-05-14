from django.contrib import admin
from django.urls import path

from devise import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:days_range>/<str:currencies>/", views.dashboard, name="home"),
]