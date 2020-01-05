from django.db import models
from accounts.models import Brewery


class Style(models.Model):
    style = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.style}'


class Flavor(models.Model):
    flavor_note = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.flavor_note}'


class GenericBeer(models.Model):
    name = models.CharField(max_length=100)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    flavor = models.ManyToManyField(Flavor)
    abv = models.FloatField()


class Beer(models.Model):
    name = models.CharField(max_length=100)
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    flavor = models.ManyToManyField(Flavor)
    abv = models.FloatField()