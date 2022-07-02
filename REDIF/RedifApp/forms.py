from http import client
from django import forms

from RedifApp.models import Redacao

class RedacaoForm(forms.ModelForm):
    class Meta:
        model = Redacao
        fields = ['titulo', 'area', 'tema', 'conteudo', 'comentario', ]
        
