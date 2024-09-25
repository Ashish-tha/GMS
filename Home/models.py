from unicodedata import name
from django.db import models
from razorpay import Payment
from traitlets import default

# Create Your Models.


class Game(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    payment = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class game1(models.Model):
    name=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    #email=models.CharField(max_length=100)
    Payment_id=models.CharField(max_length=100)
    paid=models.BooleanField(default=False)

    def __str__(self):
        return self.name
