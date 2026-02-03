from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Productos

# Create your views here.
class showProducts(TemplateView):
    template_name = 'portfolio/home.html'