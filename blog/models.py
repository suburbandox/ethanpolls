from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=100)
    textarea =models.TextField()
    last_updated = models.DateTimeField(null=True)
    last_editor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="edited_posts")
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="created_posts")

    def __str__(self):
        return self.title

