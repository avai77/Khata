from django.shortcuts import render, HttpResponse
from .models import Category, Advertisement
from .serializers import CategorySerializer, AdvertisementSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView

from rest_framework import generics
from rest_framework import mixins




class CategoryList(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializers = CategorySerializer(categories, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = CategorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class AdvertisementList(APIView):

    def get(self, request):
        advertisement = Advertisement.objects.all()
        serializers = AdvertisementSerializer(advertisement, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = AdvertisementSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class AdvertisementDetails(APIView):

    def get_object(self, id):
        try:
            return Advertisement.objects.get(id=id)

        except Advertisement.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        advertisement = self.get_object(id)
        serializers = AdvertisementSerializer(advertisement)
        return Response(serializers.data)

    def put(self, request, id):
        advertisement = self.get_object(id)
        serializer = AdvertisementSerializer(advertisement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        advertisement = self.get_object(id)
        advertisement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryDetails(APIView):

    def get_object(self, id):
        try:
            return Category.objects.get(id=id)

        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        categories = self.get_object(id)
        serializers = CategorySerializer(categories)
        return Response(serializers.data)

    def put(self, request, id):
        category = self.get_object(id)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        category = self.get_object(id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''
@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializers = CategorySerializer(categories, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = CategorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def advertisement_list(request):
    if request.method == 'GET':
        advertisement = Advertisement.objects.all()
        serializers = AdvertisementSerializer(advertisement, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = AdvertisementSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def category_details(request, pk):
    try:
        category = Category.objects.get(pk=pk)

    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def advertisement_details(request, pk):
    try:
        advertisement = Advertisement.objects.get(pk=pk)

    except advertisement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdvertisementSerializer(advertisement)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AdvertisementSerializer(advertisement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        advertisement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    '''






