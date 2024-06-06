from django.shortcuts import render
from django.http import HttpResponseNotFound

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def hackathon(request):
    return render(request, 'pages/hackathon.html')

def internship(request):
    return render(request, 'pages/internship.html')

def library(request):
    return render(request, 'pages/library.html')

def projects(request):
    return render(request, 'pages/projects.html')

def resources(request):
    return render(request, 'pages/resources.html')

def team(request):
    return render(request, 'pages/team.html')

def page_not_found(request, exception, template_name='pages/404.html'):
    return render(request,template_name)
