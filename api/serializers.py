from rest_framework import serializers
from .models import Category, Advertisement


class CategorySerializer(serializers.Serializer):
    typeOfAd = serializers.CharField(max_length=250)
    active = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Category.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.typeOfAd = validated_data.get('typeOfAd', instance.typeOfAd)
        instance.active = validated_data.get('active', instance.active)

class AdvertisementSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    image = serializers.ImageField(upload_to='media/images', blank=True)
    description = serializers.TextField(blank=True)
    phone = serializers.CharField(max_length=10, blank=True)
    price = serializers.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    category = serializers.ForeignKey(Category, on_delete=serializers.CASCADE)
    address = serializers.CharField(max_length=250, blank=True)
    year = serializers.DateTimeField()
    area = serializers.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    active = serializers.BooleanField(default=True)
    created = serializers.DateTimeField(auto_now_add=True)

    def create(self, validated_data):
        return Advertisement.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('description', instance.description)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.price = validated_data.get('price', instance.price)
        instance.category = validated_data.get('category', instance.category)
        instance.address = validated_data.get('address', instance.address)
        instance.year = validated_data.get('year', instance.year)
        instance.area = validated_data.get('area', instance.area)
        instance.active = validated_data.get('active', instance.active)
        instance.created = validated_data.get('created', instance.created)
