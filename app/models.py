from django.db import models


class Pic(models.Model):
    image = models.ImageField(upload_to='image')
    price = models.IntegerField(default=1000)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
