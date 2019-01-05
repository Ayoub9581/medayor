from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/<int:id>', views.get_profile, name='get_profile'),
]
