from django.db import models

# Create your models here.
class BlogPost(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=100)
    textarea =models.TextField()

    def __str__(self):
        return self.title

