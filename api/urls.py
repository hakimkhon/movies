from django.urls import path
from .views import FilmAPIView
urlpatterns = [
    path('', FilmAPIView.as_view())
]