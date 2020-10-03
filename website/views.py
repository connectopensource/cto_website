# Create your views here.
from django.shortcuts import render



def home_view(request):
    return render(request, 'home.html')


def about_us(request):
    return render(request, 'about.html')

def posts(request):
    return render(request , 'post_list.html')