from django.shortcuts import render
from .models import Blog
from django.views.generic import ListView, DetailView

# Create your views here.


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blog/home.html'
    ordering = ['-date']


class BlogDetailView(DetailView):
    model = Blog
