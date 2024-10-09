from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from studforce_customer.models import Customer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomerLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_superuser:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'message': 'Login successful',
                    'role': 'admin',
                    'access': str(refresh.access_token),
                    'refresh': str(refresh)
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        else:
            try:
                customer = Customer.objects.get(username=username)
                if check_password(password, customer.password):
                    refresh = RefreshToken.for_user(customer)
                    return Response({
                        'user_id': customer.id,
                        'role': 'customer',
                        'username': customer.username,
                        'access': str(refresh.access_token),
                        'refresh': str(refresh)
                    }, status=status.HTTP_200_OK)
            except Customer.DoesNotExist:
                pass

            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
