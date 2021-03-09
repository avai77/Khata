from rest_framework import serializers
from .models import Category, Advertisement
from rest_framework.serializers import Serializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'typeOfAd', 'active']

class UploadSerializer(Serializer):
    class Meta:
        fields = ['file_uploaded']


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'image', 'description', 'phone', 'price', 'category', 'address', 'year', 'area', 'active', 'created']

