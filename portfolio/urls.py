from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('', views.launch, name='launch'),
    # path('projects/create', views.create_project, name='createproject'),
    path('home/projects/', views.projects, name='projects'),
]
