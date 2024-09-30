from .models import *
from rest_framework import serializers

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

    class Meta:
        model = Product
        fields = ['name', 'description', 'brand', 'price', 'color', 'amount', 'categories', 'image', 'sizes', 'images']
