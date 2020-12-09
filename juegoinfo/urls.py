
from django.contrib import admin
from django.urls import path ,re_path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.juego.urls')),
    re_path('', include('applications.panel.urls')),
    re_path('', include('applications.user.urls')),
]
