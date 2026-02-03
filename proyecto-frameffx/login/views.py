from typing import Any
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse

class LoginFormView(LoginView):
    template_name = "portfolio/login.html"
    redirect_authenticated_user = True

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home/')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context
    
class Logout(LogoutView):
    next_page = reverse_lazy('login')
    
