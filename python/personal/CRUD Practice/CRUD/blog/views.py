from dataclasses import fields
from re import M
from django import views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from rest_framework import viewsets
from .serializers import BlogSerializer

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

class BlogUpdateview(UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'newpost.html'
    success_url = '/'


class BlogViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer