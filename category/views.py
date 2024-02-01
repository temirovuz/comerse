from django.views.generic import ListView

from .models import Category


class CategoryListView(ListView):
    model = Category
    template_name = 'category/home.html'
    context_object_name = 'categories'

