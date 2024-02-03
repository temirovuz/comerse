from django.views.generic import TemplateView

from category.models import Category


class IndexView(TemplateView):
    model = Category
    template_name = 'home.html'
    context_object_name = 'categories'
