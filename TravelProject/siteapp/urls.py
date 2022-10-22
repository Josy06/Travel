# This is siteapp's urls
# this app is created to show that we can create more than one app

from . import views
from django.urls import path
app_name='siteapp'
urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),


]
