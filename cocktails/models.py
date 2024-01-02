from django.db import models

class Cocktail(models.Model):
    name = models.CharField(max_length=255)
    primary_spirit = models.CharField(max_length=255)
    root_cocktail= models.CharField(max_length=255)
    recipe= models.TextField()

    def __str__(self):
        return self.name

