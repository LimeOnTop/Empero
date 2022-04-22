from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from .models import *


class ClothesAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'sale', 'get_html_photo', 'cat', 'available')
    list_display_links = ('title', 'sale')
    search_fields = ('title', 'price', 'id', 'description', 'available')
    list_editable = ('available',)
    list_filter = ('available', 'sale', 'cat')
    prepopulated_fields = {'slug': ('title',)}
    fields = (
        'title', 'slug', 'description', 'cat', 'photo_1', 'get_html_photo', 'photo_2', 'photo_3', 'available', 'price',
        'sale')
    readonly_fields = ('get_html_photo',)

    def get_html_photo(self, object):
        if object.photo_1:
            return mark_safe(f"<img src='{object.photo_1.url}' width=50>")

    get_html_photo.short_description = "Photo"


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}


class SizesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('id', 'name')


admin.site.register(Clothes, ClothesAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Sizes, SizesAdmin)
