from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from studforce_auth.serializers import CustomerSerializer
from studforce_customer.serializers import CustomerAddressSerializer
from django.shortcuts import get_object_or_404
from .serializers import CartSerializer

class CustomerAddressList(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomerAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerAddressDetail(APIView):
    def get(self, request, pk):
        customer_address = CustomerAddress.objects.filter(customer=pk)
        serializer = CustomerAddressSerializer(customer_address, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, pk):
        customer_address = get_object_or_404(CustomerAddress, pk=pk)
        serializer = CustomerAddressSerializer(customer_address, data=request.data, partial=True)  # ใช้ partial เพื่อให้สามารถอัปเดตข้อมูลบางส่วนได้
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        customer_address = get_object_or_404(CustomerAddress, pk=pk)
        customer_address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomerList(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CustomerRegister(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartDetail(APIView):
    def put(self, request, product_id):
        productPut = get_object_or_404(Cart, pk=product_id)
        serializer = CartSerializer(productPut, data=request.data, partial=True)  # เปิดใช้งาน partial update
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, product_id):
        productDelete = get_object_or_404(Cart, pk=product_id)
        productDelete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustomerCartList(APIView):
    def get(self, request, customer_id):
        carts = Cart.objects.filter(customer_id=customer_id)
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

