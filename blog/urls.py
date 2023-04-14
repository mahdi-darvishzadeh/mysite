from django.urls import path
from blog.views import *

app_name = 'blog'
urlpatterns = [
    path('home', blog_views, name='index'),
    path('single', blog_single, name='single'),
    path('test', test, name='test'),
]