from django.db import models


class Clothes(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    photo_1 = models.ImageField(upload_to="images")
    photo_2 = models.ImageField(upload_to="images")
    photo_3 = models.ImageField(upload_to="images")
    price = models.IntegerField()
    sale = models.IntegerField()


#class Categories(models.Model):
