from django.urls import path

from .views import Register, Login_user, Logout_user

app_name = 'account'

urlpatterns = [
    path('register/', Register, name='register'),
    path('login/', Login_user, name='login'),
    path('login/', Logout_user, name='logout'),

]
