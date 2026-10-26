from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(255)


class Movie(models.Model):
    title = models.CharField(255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rental_rate = models.FloatField()
    genre = models.ForeignKey(Genre , on_delete=models.CASCADE)