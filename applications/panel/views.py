from django.shortcuts import render

# Create your views here.
from django.views.generic import  TemplateView


from applications.juego.models import Juego


class Panel(TemplateView):
    template_name = "panel/index.html"

    
    
    def get_context_data(self, **kwargs):
        context = super(Panel, self).get_context_data(**kwargs)
        kword = self.request.GET.get("kword", '')
        context['juegos'] = Juego.objects.search_juego(kword)
        

        return context

    