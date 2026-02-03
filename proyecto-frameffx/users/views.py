from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
    ListView
)

from .models import Usuario
from .mixins import StaffRequiredMixin, SetPasswordMixin


class UsuariosListView(StaffRequiredMixin, ListView):
    model = Usuario
    template_name = "users/usuarios_list.html"
    context_object_name = "usuarios"

class UsuariosCreateView(StaffRequiredMixin, SetPasswordMixin, CreateView):
    model = Usuario
    fields = ["username", "email", "activo"]
    template_name = "users/usuarios_form.html"
    success_url = reverse_lazy("usuarios_list")

class UsuariosUpdateView(StaffRequiredMixin, SetPasswordMixin, UpdateView):
    model = Usuario
    fields = ["nombre", "email", "rol"]
    template_name = "users/usuarios_form.html"
    success_url = reverse_lazy("usuarios_list")

class UsuariosDeleteView(StaffRequiredMixin, DeleteView):
    model = Usuario
    template_name = "users/usuarios_confirm_delete.html"
    success_url = reverse_lazy("usuarios_list")

class HomeView(TemplateView):
    template_name = "portfolio/home.html"
    login_url = '/'

class LoginView(TemplateView):
    template_name = "portfolio/login.html"
