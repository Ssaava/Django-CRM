from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name="home"),
    path('hackathon/', views.hackathon, name="hackathon"),
    path('internship/', views.internship, name="internship"),
    path('library/', views.library, name="library"),
    path('projects/', views.projects, name="projects"),
    path('resources/', views.resources, name="resources"),
    path('team/', views.team, name="team"),
    path('404/', views.page_not_found, name="404"),

]
