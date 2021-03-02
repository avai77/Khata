from django.urls import path
from .views import category_list, advertisement_list, category_details, advertisement_details


urlpatterns = [
    path('categories/', category_list),
    path('categories/<int:pk>/', category_details),
    path('ads/', advertisement_list),
    path('ads/<int:pk>/', advertisement_details),
]
