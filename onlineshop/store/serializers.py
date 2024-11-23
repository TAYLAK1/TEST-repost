from rest_framework import serializers
from unicodedata import category

from .models import  Category, Product

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'have', 'price',
                  'created_date', 'image', 'video']