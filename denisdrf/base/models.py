from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)


class Car(Item):
    max_speed = models.IntegerField(default=0)

