from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.viewsets import ViewSet

from .models import Category, Advertisement
from .serializers import CategorySerializer, AdvertisementSerializer, UploadSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication,)

class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    authentication_classes = (TokenAuthentication,)










