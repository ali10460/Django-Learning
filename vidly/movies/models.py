from django.db import models
from django.utils import timezone

# Create your models here.


class Genre(models.Model):
    name = models.CharField(255)

    def __str__(
        self,
    ):  # this method change the object of the genre into the string in django admin
        return self.name


class Movie(models.Model):
    title = models.CharField()
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rental_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
