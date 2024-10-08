from rest_framework import serializers
from .models import Product, ProductSize, ProductImage, ProductCategory

class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['type_size', 'size']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['name']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    sizes = ProductSizeSerializer(many=True, read_only=True, source='size')
    categories = serializers.SlugRelatedField(
        many=True, 
        read_only=True, 
        slug_field='name'
    )
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'brand', 'price', 'color', 'amount', 'categories', 'image', 'sizes', 'images']
