from django.urls import path
from . import views

urlpatterns = [
    path("", views.guest_dashboard, name="guest_dashboard"),
]