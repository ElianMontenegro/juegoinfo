from django.urls import path

from . import views

app_name = "juego_app"

urlpatterns = [
    path(
        'list', 
        views.JuegoListView.as_view(),
        name='juego',
    ),
]