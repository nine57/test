from django import db
from django.db import models

# Create your models here.
class Menus(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'menus'

class Categories(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menus', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Drinks(models.Model):
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)

    class Meta:
        db_table = 'drinks'

class Allergens_drinks(models.Model):
    allergen = models.ForeignKey("Allergens", on_delete=models.CASCADE)
    drink = models.ForeignKey("Drinks", on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergens_drinks'

class Allergens(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'allergens'
