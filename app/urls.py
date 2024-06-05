from django.urls import path
from . import views

app_name = 'app'
handler404 = "app.views.page_not_found"
urlpatterns = [
    path('', views.index, name="index"),
    path('404/', views.page_not_found, name="404")
]
