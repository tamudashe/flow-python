# algotutor/models.py

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    # tells python how to represent this object
    def __str__(self):
        return self.title