from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=100)
    rejisor = models.CharField(max_length=100)
    type_film = models.CharField(max_length=50)
    about_film = models.CharField(max_length=500)
    pochta = models.EmailField(max_length=100)

    def __str__(self):
        return self.title
    