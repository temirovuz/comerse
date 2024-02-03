from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('account/', include('account.urls')),
    path('', include("django.contrib.auth.urls")),
    path('category/', include('category.urls')),
    path('order/', include('order.urls')),
    path('product/', include('product.urls')),

]
