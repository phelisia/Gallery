from django.db import models
import datetime as dt


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length =50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Location(models.Model):
    name = models.CharField(max_length =70)
    @classmethod
    def get_locations(cls):
         location = Location.objects.all()
         return locations
    def __str__(self):
        return self.name




