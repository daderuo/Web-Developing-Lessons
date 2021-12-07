from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=64)
    bed = models.IntegerField()    

    def __str__(self):
        return f"Room name: {self.name}, bed number: {self.bed}"

class Hotel(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE,related_name="room_name")
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.room}, available: {self.available}"

class Guest(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    booked_room = models.ManyToManyField(Hotel,blank=True,related_name="b_room")

    def __str__(self):
        return f"Guest: {self.first_name} {self.last_name}"