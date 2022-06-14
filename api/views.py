from film.models import Film
from .serializers import FilmSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView

class ListFilm(ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class DetailFilm(RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
