from datetime import datetime

from django.db import models


class Comic(models.Model):
    name = models.CharField(max_length=1000)
    types = models.CharField(max_length=100)
    excerpt = models.TextField(max_length=200)
    description = models.TextField()
    picture = models.ImageField(upload_to='comic_picture')

    def __str__(self):
        return self.name


class DetailComic(models.Model):
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    types = models.CharField(max_length=50)
    description = models.TextField()
    avatar = models.ImageField(upload_to='avatar_comic')

    def __str__(self):
        return self.name


class TableChap(models.Model):
    chapComic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    stt = models.PositiveSmallIntegerField(default=0)
    chapSo = models.PositiveSmallIntegerField(default=0)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class ViewComic(models.Model):
    viewChap = models.ForeignKey(TableChap, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    anhChap = models.ImageField(upload_to='chap_image')

    def __str__(self):
        return self.name
