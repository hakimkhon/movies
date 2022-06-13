from rest_framework import serializers
from film.models import Film

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'title', 'rejisor', 'type_film', 'about_film', 'pochta')

