from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
User = get_user_model()
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

class StaffLoginView(LoginView):

    template_name = "staff_management/login.html"

    def get_success_url(self):
        return reverse_lazy("staff_dashboard")


class StaffLogoutView(LogoutView):
    next_page = reverse_lazy("staff_login")

class StaffDashboardView(LoginRequiredMixin,UserPassesTestMixin,TemplateView):

    template_name = "staff_management/dashboard.html"

    login_url = reverse_lazy("staff_login")

    def test_func(self):
        return self.request.user.is_staff
    