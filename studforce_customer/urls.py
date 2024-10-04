from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductList.as_view(), name='product-detail'),
    path('customer/', CustomerRegList.as_view(), name='customer-list'),
    path('login/', CustomerLoginView.as_view(), name='login'),
]