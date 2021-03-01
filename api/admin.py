from django.contrib import admin
from .models import Category, Advertisement

# Register your models here.

# admin.site.register(Category)

@admin.register(Category)
class CategoryModel(admin.ModelAdmin):
    list_filter = ('typeOfAd', 'active')
    list_display = ('typeOfAd', 'active')

@admin.register(Advertisement)
class AdvertisementModel(admin.ModelAdmin):
     list_filter = ('title', 'image', 'description', 'phone', 'price', 'category', 'address', 'year', 'area', 'active', 'created')
     list_display = ('title', 'image', 'description', 'phone', 'price', 'category', 'address', 'year', 'area', 'active', 'created')
