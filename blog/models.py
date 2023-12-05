from django.db import models

# Create your models here.
class BlogPost(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=100)
    textarea =models.TextField()
    last_updated = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

