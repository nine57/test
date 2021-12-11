from django import db
from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'menus'
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'
    def __str__(self):
        return self.name

class Allergen(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'allergens'
    def __str__(self):
        return self.name

class Drink(models.Model):
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'drinks'
    def __str__(self):
        return self.korean_name

class Allergen_drink(models.Model):
    allergen = models.ForeignKey('Allergen', on_delete=models.CASCADE)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergens_drinks'

class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=10, decimal_places=2, null= True)
    sodium_mg = models.DecimalField(max_digits=10, decimal_places=2, null= True)
    saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=2, null= True)
    sugars_g = models.DecimalField(max_digits=10, decimal_places=2, null= True)
    protein_g = models.DecimalField(max_digits=10, decimal_places=2, null= True)
    caffeine_mg = models.DecimalField(max_digits=10, decimal_places=2, null= True)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE, null= True)
    size = models.ForeignKey('Size', on_delete=models.CASCADE, null= True)

    class Meta:
        db_table = 'nutritions'

class Size(models.Model):
    name = models.CharField(max_length=45)
    size_ml = models.CharField(max_length=45, null= True)
    size_fluid_ounce = models.CharField(max_length=45, null= True)  

    class Meta:
        db_table = 'sizes'
    def __str__(self):
        return self.name

class Test(models.Model):
    test = models.CharField(max_length=20)