from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'birthdate', 'email', 'phone', 'username', 'password', 'gender']
    
    def validate_password(self, value):
        return make_password(value)
