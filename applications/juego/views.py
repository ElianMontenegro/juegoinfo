from django.shortcuts import render

from django.urls import reverse_lazy, reverse
# Create your views here.

from django.views.generic import (
    View,
    CreateView,
    ListView
)

from .forms import FormJuego
from .models import Juego



class JuegoListView(ListView):
    model = Juego
    template_name = "juego/list.html"
