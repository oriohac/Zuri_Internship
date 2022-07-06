from dataclasses import fields
from re import M
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from .models import Post

# Create your views here.
class BlogListview(ListView):
    model = Post
    fields = [
        'topic',
        'body'
    ]
    template_name = 'list.html'

class BlogCreateview(CreateView):
    model = Post
    fields = '__all__'
    template_name = 'newpost.html'
    success_url = '/'

class BlogDeleteview(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = '/'
