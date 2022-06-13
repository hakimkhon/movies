from django.views.generic import ListView, DetailView
from .models import Film

class FilmListView(ListView):
    model = Film
    template_name = "film_app/film_list.html" 

class FilmDetailView(DetailView):
    model = Film
    template_name = "film_app/film_detail.html"
