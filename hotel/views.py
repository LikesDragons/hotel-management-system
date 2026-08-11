from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from django.contrib.auth import get_user_model
User = get_user_model()
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

class GuestDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "guest_management/guest_dashboard.html"

    login_url = reverse_lazy("guest_login")

from hotel.forms import GuestSignupForm

class GuestSignupView(CreateView):
    model = User
    form_class = GuestSignupForm
    template_name = "guest_management/signup.html"
    success_url = reverse_lazy("guest_login")


class GuestLoginView(LoginView):
    template_name = "guest_management/login.html"
    redirect_authenticated_user = True

    def form_valid(self, form):
        if form.get_user().is_staff:
            form.add_error(None, "Please use the staff login page.")
            return self.form_invalid(form)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("home")


class GuestLogoutView(LogoutView):
    next_page = reverse_lazy("guest_login")

