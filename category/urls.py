from django.urls import path

from category.views import CategoryListView, SubCategoryListView

app_name = 'category'

urlpatterns = [
    path('', CategoryListView.as_view(), name='category-list'),
    path('<slug:slug>/', SubCategoryListView.as_view(), name='sub-category')
]
