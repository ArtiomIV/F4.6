from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'recipes', RecipesViewset)
router.register(r'categories', CatigoriesViewset)
router.register(r'products', ProductsViewset)
router.register(r'recipeproduct', RecipeProductViewses)

urlpatterns = [
    path('', include(router.urls))
]
