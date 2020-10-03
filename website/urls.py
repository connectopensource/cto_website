from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about_us, name='about'),
    path('', views.home_view, name='home'),
    path('posts' , views.posts , name='posts')
] 