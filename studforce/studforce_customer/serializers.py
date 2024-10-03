from .models import *
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'birthdate', 'email', 'phone', 'username', 'password', 'gender']
    
    def validate_password(self, value):
        return make_password(value)

class ProductSizeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['type_size', 'size']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    sizes = ProductSizeSerializers(many=True, read_only=True, source='size')
    categories = serializers.SlugRelatedField(
            many=True, 
            read_only=True, 
            slug_field='name'
        )
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'brand', 'price', 'color', 'amount', 'categories', 'image', 'sizes', 'images']
