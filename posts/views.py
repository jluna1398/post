from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = "home.html"