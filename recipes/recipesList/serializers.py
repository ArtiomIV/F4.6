from .models import *
from rest_framework import serializers

class ReciperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'price', 'category', 'products', 'desc']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

class RecipeProducySerialaizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RecipeProduct
        fields = ['product', 'recipe', 'amount']