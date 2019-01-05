from django.urls import path
from . import views

urlpatterns = [
    path('', views.launch, name='launch'),
    path('home/', views.index, name='home'),
    path('projects/',views.projects, name='projects'),
]
