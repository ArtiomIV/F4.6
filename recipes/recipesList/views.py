from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from recipesList.serializers import *
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class RecipesViewset(viewsets.ModelViewSet):
    queryset = Recipe.objects.order_by('-price')
    serializer_class = ReciperSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'name']

class CatigoriesViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductsViewset(viewsets.ModelViewSet):
    queryset = Product.objects.order_by('-price')
    serializer_class = ProductSerializer

class RecipeProductViewses(viewsets.ModelViewSet):
    queryset = RecipeProduct.objects.all()
    serializer_class = RecipeProducySerialaizer