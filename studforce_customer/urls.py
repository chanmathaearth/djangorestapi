from django.urls import path
from .views import CustomerListView, CustomerRegisterView

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer-list'),
    path('register/', CustomerRegisterView.as_view(), name='customer-register'),
]
