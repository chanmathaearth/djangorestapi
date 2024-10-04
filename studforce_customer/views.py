from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate

class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all().order_by('id')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product_data = serializer.validated_data

            sizes_data = request.data.get('sizes', [])
            images_data = request.data.get('images', [])
            categories_data = request.data.get('categories', [])

            product = Product.objects.create(
                name=product_data['name'],
                description=product_data['description'],
                brand=product_data['brand'],
                price=product_data['price'],
                color=product_data['color'],
                image=product_data['image'],
                amount=product_data['amount']
            )

            for category_name in categories_data:
                category_instance = ProductCategory.objects.get(name=category_name)
                product.categories.add(category_instance)

            for size_data in sizes_data:
                ProductSize.objects.create(product=product, **size_data)

            for image_data in images_data:
                ProductImage.objects.create(product=product, **image_data)

            return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            product_data = serializer.validated_data
            product.name = product_data.get('name', product.name)
            product.description = product_data.get('description', product.description)
            product.brand = product_data.get('brand', product.brand)
            product.price = product_data.get('price', product.price)
            product.color = product_data.get('color', product.color)
            product.image = product_data.get('image', product.image)
            product.amount = product_data.get('amount', product.amount)
            product.save()

            categories_data = request.data.get('categories', [])
            if categories_data:
                product.categories.clear()
                for category_name in categories_data:
                    category_instance= ProductCategory.objects.get(name=category_name)
                    product.categories.add(category_instance)

            sizes_data = request.data.get('sizes', [])
            if sizes_data:
                product.size.all().delete()
                for size_data in sizes_data:
                    ProductSize.objects.create(product=product, **size_data)

            images_data = request.data.get('images', [])
            if images_data:
                product.images.all().delete()
                for image_data in images_data:
                    ProductImage.objects.create(product=product, **image_data)

            return Response(ProductSerializer(product).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomerRegList(APIView):
    def get(self, request):
        customer = Customer.objects.all()
        serializer = CustomerSerializers(customer, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CustomerSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_superuser:
                return Response({'message': 'Login successful', 'role': 'admin'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        else:
            try:
                customer = Customer.objects.get(username=username)
                if check_password(password, customer.password):
                    return Response({'message': 'Login successful', 'role': 'customer', 'user_id': customer.id, 'username': customer.username}, status=status.HTTP_200_OK)
            except Customer.DoesNotExist:
                pass

            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)