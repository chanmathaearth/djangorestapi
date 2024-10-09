from rest_framework import serializers
from .models import CustomerAddress, Order, ProductOrder, Cart
from studforce_auth.models import Customer

from studforce_product.serializers import ProductSerializer

class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = ['id', 'customer', 'street_address', 'province', 'district', 'subdistrict', 'postal_code', 'phone_number']

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    promotion = serializers.StringRelatedField()
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'products', 'total_price', 'order_status', 'payment_status', 'created_at', 'promotion']

class ProductOrderSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    order = serializers.StringRelatedField()

    class Meta:
        model = ProductOrder
        fields = ['order', 'product', 'amount', 'price']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'customer', 'product', 'amount', 'type_size', 'size']
