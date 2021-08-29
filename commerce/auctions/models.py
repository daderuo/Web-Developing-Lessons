from django.contrib.auth.models import AbstractUser
from django.db import models

cat = (
    ('Fashion','Fashion'),
    ('Tool','Tool'),
    ('Electronic','Electronic'),
    ('Garden','Garden'),
    ('Toy','Toy'),
    ('Car','Car')
)

class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_price = models.FloatField()
    current_price = models.FloatField()
    final_price = models.FloatField()
    image = models.ImageField(upload_to='photo/')
    category = models.CharField(choices=cat, max_length=20)
    active = models.BooleanField(default=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="auction")

    def __str__(self):
        return f"{self.title}: {self.description}. Start Price: {self.start_price}, Current Price: {self.current_price}, Final Price: {self.final_price}. Category: {self.category}, Active: {self.active}"


class Bids(models.Model):
    pass 

class Comments(models.Model):
    pass 
