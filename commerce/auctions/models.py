from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='photo/')
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title}: {self.description}. Price: {self.price}. Category: {self.category}"

class Bids(models.Model):
    pass 

class Comments(models.Model):
    pass 
