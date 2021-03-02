from django.urls import path, include
from .views import CategoryViewSet,AdvertisementViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('ads', AdvertisementViewSet, basename='ads')


urlpatterns = [
    path('', include(router.urls)),

]
