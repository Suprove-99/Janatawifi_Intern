from django.shortcuts import render
from .models import MyModel
from django.views.generic import TemplateView, ListView


class HomePageView(ListView):
    model = MyModel
    template_name = 'home.html'
