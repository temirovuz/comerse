from django.db.models import Q
from django.views.generic import ListView

from product.models import Product
from .models import Category


class CategoryListView(ListView):
    model = Category
    template_name = 'category/home.html'
    context_object_name = 'categories'


class SubCategoryListView(ListView):
    model = Category
    context_object_name = 'sub_categories'
    template_name = 'category/sub_categpry.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        qs = super().get_queryset()
        return qs.filter(parent__slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        slug = self.kwargs['slug']
        context['products'] = Product.objects.filter(Q(category__slug=slug) | Q(category__parent__slug=slug))

        return context
