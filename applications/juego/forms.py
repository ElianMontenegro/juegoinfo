from django import forms

from .models import Juego 

class FormJuego(forms.ModelForm):
  
    class Meta:
        model = Juego

        fields=('__all__')

