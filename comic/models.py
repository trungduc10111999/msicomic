from django.db import models


class Comic(models.Model):
    name = models.CharField(max_length=1000)
    types = models.CharField(max_length=100)
    excerpt = models.TextField(max_length=200)
    description = models.TextField()
    picture = models.ImageField(upload_to='comic_picture')

    def __str__(self):
        return self.name
