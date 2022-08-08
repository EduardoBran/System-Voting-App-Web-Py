from django.shortcuts import render
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'main/mainIndex.html'


class SobreView(TemplateView):
    template_name = 'main/sobre.html'

# Create your views here.
