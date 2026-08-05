from django.urls import path
from . import views

urlpatterns = [
    #path("", views.guest_dashboard, name="guest_dashboard"),
    path("", views.GuestDashboardView.as_view(), name="home"),

    path("signup/", views.GuestSignupView.as_view(), name="guest_signup"),

    path("login/", views.GuestLoginView.as_view(), name="guest_login"),

    path("logout/", views.GuestLogoutView.as_view(), name="guest_logout"),

    path("dashboard/", views.GuestDashboardView.as_view(), name="guest_dashboard"),

    path("staff/dashboard/", views.StaffDashboardView.as_view(), name="staff_dashboard"),

    path("staff/login/", views.StaffLoginView.as_view(), name="staff_login"),

    path("staff/logout/", views.StaffLogoutView.as_view(), name="staff_logout"),
]