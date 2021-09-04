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



class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_price = models.FloatField()
    current_price = models.FloatField()
    final_price = models.FloatField()
    image = models.ImageField(upload_to='photo/')
    category = models.CharField(choices=cat, max_length=20)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}: {self.description}. Start Price: {self.start_price}, Current Price: {self.current_price}, Final Price: {self.final_price}. Category: {self.category}, Active: {self.active}"

class User(AbstractUser):
    auctions = models.ManyToManyField(Listing, blank=True, related_name='creator')
    watchlist = models.ManyToManyField(Listing, blank=True, related_name='watchlist')
    winner = models.ManyToManyField(Listing, blank=True, related_name="winner")

class Bids(models.Model):
    value = models.FloatField()
    auction = models.ForeignKey(Listing, on_delete=models.CASCADE,related_name='bid')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bid')

    def __str__(self):
        return f" Value: {self.value}, Auction: {self.auction.title}, User: {self.user}"


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="comment", default=None) 
    text = models.TextField(default=None)
    auction = models.ForeignKey(Listing, on_delete=models.CASCADE,related_name="comment", default=None)

    def __str__(self) :
        return f"User: {self.user} Text: {self.text} Auction: {self.auction.title}"
