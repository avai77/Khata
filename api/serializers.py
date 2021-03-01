from rest_framework import serializers
from .models import Category, Advertisement


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'typeOfAd', 'active']


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'image', 'description', 'phone', 'price', 'category', 'address', 'year', 'area', 'active', 'created']

