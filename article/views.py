from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Sample
from django.urls import reverse_lazy

# Create your views here.

class HomePage(ListView):
    template_name = 'home.html'
    model = Sample


class DetailsPage(DetailView):
    template_name = 'details.html'
    model  = Sample


class CreatePage(CreateView):
    template_name = 'create.html'
    model= Sample
    fields = ['title', 'author', 'body']


class UpdatePage(UpdateView):
    template_name = 'update.html'
    model = Sample
    fields = ['title', 'author', 'body']

class DeletePage(DeleteView):
    template_name = 'delete.html'
    model = Sample
    fields = ['title', 'author', 'body']
    success_url = reverse_lazy('home')