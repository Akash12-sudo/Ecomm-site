from django.db import models

# Create your models here.

class Product(models.Model):

    title = models.CharField(max_length= 200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=400)


    def __str__(self):
        return self.title


class Order(models.Model):

    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=20)
    total = models.FloatField(default=0)

    def __str__(self):
        return self.name
