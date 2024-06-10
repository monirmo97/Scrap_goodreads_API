from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    average_rating = models.FloatField()
    total_ratings = models.IntegerField()
    edition_number = models.IntegerField()
    publish_year = models.IntegerField()

    def __str__(self):
        return self.title

