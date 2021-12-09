from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime,timezone


class User(AbstractUser):
    pass

class Net(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed")

    def __str__(self):
        return f" {self.followed} is followed by {self.follower}"

class Post(models.Model):
    text = models.TextField()
    date_time = models.DateTimeField(default=datetime.now(timezone.utc))
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Post')
    like = models.ManyToManyField(User, blank=True, related_name="like")

    class Meta:
        ordering = ['-date_time']
    
    def __str__(self):
        return f" {self.text}, {self.date_time}, {self.author}"


