from django.contrib import admin

# Register your models here.
from .models import *


class ClothesAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'sale', 'cat', 'picked')
    list_display_links = ('title', 'sale')
    search_fields = ('title', 'price', 'id', 'description', 'picked')
    list_editable = ('picked',)
    list_filter = ('picked', 'sale', 'cat')
    prepopulated_fields = {'slug': ('title',)}


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Clothes, ClothesAdmin)
admin.site.register(Categories, CategoriesAdmin)
