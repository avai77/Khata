from rest_framework import serializers
from .models import Category, Advertisement
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'typeOfAd', 'active']

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'image', 'description', 'phone', 'price', 'category', 'address', 'year', 'area', 'active', 'created']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        extra_kwargs = {'password':{
            'write_only':True,
            'required':True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user