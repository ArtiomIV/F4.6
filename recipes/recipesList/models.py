from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(
        max_length = 20,
        unique = True
    )
    price = models.FloatField(default = 0.0, null = True)
    category = models.ForeignKey('Category', on_delete = models.CASCADE)
    products = models.ManyToManyField('Product', through = 'RecipeProduct')
    desc = models.TextField(max_length = 300)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self): # function to invoke url
        return f'/recipe/{self.id}'
    

class Category(models.Model):
    name = models.CharField(
        max_length=20,
        unique = True
    )

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(
        max_length = 20,
        unique = True
    )
    price = models.FloatField(default = 0.0, null = True)

    def __str__(self):
        return f'{self.name}'

class RecipeProduct(models.Model):
    product = models.ForeignKey('Product', on_delete = models.CASCADE)
    recipe = models.ForeignKey('Recipe', on_delete = models.CASCADE)
    amount = models.FloatField(default = 0.0, null = True)