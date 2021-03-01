from django.contrib import admin
from .models import Category

# Register your models here.

# admin.site.register(Category)

@admin.register(Category)
class CategoryModel(admin.ModelAdmin):
    list_filter = ('typeOfAd', 'active')
    list_display = ('typeOfAd', 'active')
