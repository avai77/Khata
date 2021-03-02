from django.urls import path
from .views import CategoryList, CategoryDetails, AdvertisementDetails, AdvertisementList
#category_list, advertisement_list, category_details, advertisement_details

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('categories/<int:id>/', CategoryDetails.as_view()),
    path('ads/', AdvertisementList.as_view()),
    path('ads/<int:id>/', AdvertisementDetails.as_view()),

    # path('categories/', category_list),
    # path('categories/<int:pk>/', category_details),
    # path('ads/', advertisement_list),
    # path('ads/<int:pk>/', advertisement_details),
]
