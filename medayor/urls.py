from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
# from . import views

handler404 = 'medayor.views.error_views.view_404'
handler500 = 'medayor.views.error_views.view_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('portfolio.urls')),
    path('services/', include('services.urls')),
] + static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)
