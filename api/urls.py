from django.urls import path
from .views import ListFilm, DetailFilm
urlpatterns = [
    path('', ListFilm.as_view()),
    path('<int:pk>/', DetailFilm.as_view()),
]