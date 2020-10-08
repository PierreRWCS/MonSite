from django.db import models

class ingredients(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class produits(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ForeignKey(ingredients, on_delete=models. CASCADE)

    def __str__(self):
        return self.name