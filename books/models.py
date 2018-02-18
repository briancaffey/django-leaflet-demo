from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=300)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.title