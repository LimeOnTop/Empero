from django.db import models
from django.urls import reverse


class Clothes(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    photo_1 = models.ImageField(upload_to="images")
    photo_2 = models.ImageField(upload_to="images")
    photo_3 = models.ImageField(upload_to="images")
    price = models.IntegerField()
    sale = models.IntegerField()
    cat = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True)

    def get_id(self):
        return reverse('description', kwargs={'card_id': self.pk})


class Categories(models.Model):
    name = models.CharField(max_length=100, db_index=True)
