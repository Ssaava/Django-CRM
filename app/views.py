from django.shortcuts import render
from django.http import HttpResponseNotFound

# Create your views here.
def index(request):
    return render(request,'pages/home.html')

def page_not_found(request, exception, template_name='pages/404.html'):
    return render(request,template_name)
