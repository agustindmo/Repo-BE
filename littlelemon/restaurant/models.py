from django.db import models
from datetime import datetime

# Create your models here.
class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField(default=datetime.now())

class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    inventory = models.IntegerField()

    def __str__(self):
         return f'{self.title} : {str(self.price)}'

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'