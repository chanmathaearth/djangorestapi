from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
]