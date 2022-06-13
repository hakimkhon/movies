from rest_framework.generics import ListAPIView, RetrieveAPIView
from film.models import Film
from .serializers import FilmSerializer

class ListFilm(ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class DetailFilm(RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
