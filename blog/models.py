from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    article = models.TextField()
    date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.author
