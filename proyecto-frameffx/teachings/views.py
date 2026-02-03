from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Teaching

# Create your views here.
class showTeachings(TemplateView):
    template_name = 'portfolio/home.html'

    def get_context_data(self, **kwargs):
        context = super(showTeachings,self).get_context_data(**kwargs)
        clase = self.request.GET.get("titulo",'')
        if clase:
            context["teachings"]=Teaching.objects.filter(title_teaching__icontains=clase)
        else:
            context["teachings"]=Teaching.objects.all()
        marcado_vista = self.request.GET.get("marcado", "")
        if marcado_vista == 'True':
            context["teachings"] = context["teachings"].order_by("nombre")
        context["marcado"]= marcado_vista

        

        return context  
         
