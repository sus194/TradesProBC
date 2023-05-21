# appname/models.py

from django.db import models
from django.contrib.auth.models import User

class Trade(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    hourly_salary = models.DecimalField(max_digits=6, decimal_places=2)
    operating_areas = models.ManyToManyField('Location')

class Location(models.Model):
    name = models.CharField(max_length=100)

class Rating(models.Model):
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()

class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
