from django.urls import path

from category.views import CategoryListView

app_name = 'category'

urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list')
]
