import imp
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from film.models import Film
from .serializer import FilmSerializer


class FilmAPIView(ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer 
