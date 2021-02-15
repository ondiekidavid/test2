from rest_framework import serializers
from .models import Customer
from .models import Order
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    E_shop = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())

    class Meta:
        model = User
        fields = ['id', 'Name', 'E_shop']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'Name', 'Code', 'email']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'item', 'amount', 'date']


