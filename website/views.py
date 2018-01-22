# Create your views here.
from django.shortcuts import render


def post_list(request):
    return render(request, 'website/post_list.html', {})


def home_view(request):
    return render(request, 'website/home.html')


def about_us(request):
    return render(request, 'website/about.html')


