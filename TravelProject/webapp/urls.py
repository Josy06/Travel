# This is webapp url
from . import views
from django.urls import path

app_name='webapp'
urlpatterns = [
    path('', views.home, name='out'),
    path('news', views.news, name='news'),
    path('home', views.home, name='home'),
    path('elements',views.elements,name='elements'),
    path('contact',views.contact,name='contact'),
    path('destinations',views.destinations,name='destinations')

]
