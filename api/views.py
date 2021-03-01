from django.shortcuts import render, HttpResponse
from .models import Category, Advertisement
from .serializers import CategorySerializer, AdvertisementSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.

def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializers = CategorySerializer(categories, many=True)
        return JsonResponse(serializers.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = CategorySerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, status=201)
        return JsonResponse(serializers.errors, status=400)

def advertisement_list(request):
    if request.method == 'GET':
        advertisement = Advertisement.objects.all()
        serializers = AdvertisementSerializer(advertisement, many=True)
        return JsonResponse(serializers.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = AdvertisementSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return JsonResponse(serializers.data, status=201)
        return JsonResponse(serializers.errors, status=400)



