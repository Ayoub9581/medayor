from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.services_home, name='services'),
    path('services/create',views.add_service, name='createservice'),
    path('service/<slug:slug>/',views.service_detail, name='detail'),
]
