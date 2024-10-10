from django.urls import path
from .views import CustomerList, CustomerRegister, CartDetail, CustomerCartList, CustomerAddressList, CustomerAddressDetail, charge_customer

urlpatterns = [
    path('', CustomerList.as_view(), name='customer-list'),
    path('register/', CustomerRegister.as_view(), name='customer-register'),
    path('cart/<int:product_id>/', CartDetail.as_view(), name='cart-detail'),
    path('customer-cart/', CustomerCartList.as_view(), name='customer-cart'),
    path('customer-cart/<int:customer_id>/', CustomerCartList.as_view(), name='customer-cart'),
    path('customer-addresses/', CustomerAddressList.as_view(), name='customer-address-list-create'),
    path('customer-addresses/<int:pk>/', CustomerAddressDetail.as_view(), name='customer-address-detail'),
    path('charge/', charge_customer, name='charge_customer'),

]
