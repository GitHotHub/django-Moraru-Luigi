from typing import Match
from django.db import models
from django.db.models.base import Model

# Create your models here.
class Giornalista(models.Model):
    nome = models.CharField(max_length=26)
    cognome = models.CharField(max_length=26)

    def __str__(self):
        return self.nome + " " + self.cognome

class Articolo(models.Model):
    titolo = models.CharField(max_length=100)
    contenuto = models.TextField()
    giornalista = models.ForeignKey(Giornalista, on_delete=models.CASCADE, related_name="articoli")

    def __str__(self):
        return self.titolo