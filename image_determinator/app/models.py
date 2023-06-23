from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    result = models.CharField(max_length=200, blank=True)
