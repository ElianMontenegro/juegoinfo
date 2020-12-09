from django.urls import path

from . import views

app_name = "panel_app"

urlpatterns = [
    path(
        '', 
        views.Panel.as_view(),
        name='index',
    ),
    
]