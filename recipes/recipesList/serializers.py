from .models import *
from rest_framework import serializers
   
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

class RecipeProducySerialaizer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    recipe = serializers.StringRelatedField()

    class Meta:
        model = RecipeProduct
        fields = ['product', 'recipe', 'amount']

class ReciperSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    products = RecipeProducySerialaizer(source='recipeproduct_set', many = True)

    class Meta:
        model = Recipe
        fields = '__all__'