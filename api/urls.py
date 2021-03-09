from django.urls import path, include
from .views import CategoryViewSet, AdvertisementViewSet, UploadViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register(r'ads', AdvertisementViewSet, basename='ads')
router.register(r'upload', UploadViewSet, basename="upload")


urlpatterns = [
    path('', include(router.urls)),

]
