from django.shortcuts import render
from django.views import generic

from category.models import Category


class HomeView(generic.ListView):
    model = Category
    template_name = 'home.html'
