from django.shortcuts import render
from django.urls import reverse_lazy

from .models import MyModel
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView


class HomePageView(ListView):
    model = MyModel
    template_name = 'home.html'



class CreateRowView(CreateView):
    model = MyModel
    template_name = 'create.html'
    fields = ['date', 'trade_code', 'high', 'low', 'open', 'close', 'volume']


class UpdateRowView(UpdateView):
    model = MyModel
    template_name = 'update.html'
    fields = ['date', 'trade_code', 'high', 'low', 'open', 'close', 'volume']


class DeleteRowView(DeleteView):
    model = MyModel
    template_name = 'delete.html'
    success_url = reverse_lazy('home_')
