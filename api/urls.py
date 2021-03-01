from django.urls import path
from .views import category_list, advertisement_list


urlpatterns = [
    path('categories/', category_list),
    path('advirtesements/', advertisement_list),
]
