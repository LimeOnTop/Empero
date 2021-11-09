from django.db import models
from django.urls import reverse


class Clothes(models.Model):
    title = models.CharField(max_length=255, verbose_name='Name')
    description = models.TextField(blank=True, verbose_name='Description')
    photo_1 = models.ImageField(upload_to="images", verbose_name='Photo 1')
    photo_2 = models.ImageField(upload_to="images", verbose_name='Photo 2')
    photo_3 = models.ImageField(upload_to="images", verbose_name='Photo 3')
    price = models.IntegerField(verbose_name='Price')
    sale = models.IntegerField(verbose_name='Sale')
    picked = models.BooleanField(default=False, verbose_name='Picked')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    cat = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True, verbose_name='Category')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('description', kwargs={'card_slug': self.slug})

    class Meta:
        verbose_name = 'Cloth'
        verbose_name_plural = 'Clothes'
        ordering = ['title', 'price']


class Categories(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Category')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name', ]
