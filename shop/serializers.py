
from rest_framework import serializers
from .models import Product


    # title = models.CharField(max_length= 200)
    # price = models.FloatField()
    # discount_price = models.FloatField()
    # category = models.CharField(max_length=200)
    # description = models.TextField()
    # image = models.CharField(max_length=400)

class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product

        fields = ['id', 'title', 'price', 'discount_price', 'category', 'description', 'image']
