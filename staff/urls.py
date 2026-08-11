from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.StaffLoginView.as_view(), name="staff_login"),
    path("logout/", views.StaffLogoutView.as_view(), name="staff_logout"),
    path("dashboard/", views.StaffDashboardView.as_view(), name="staff_dashboard"),
]