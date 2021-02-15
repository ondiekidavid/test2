from .models import Customer
from .models import Order
from .serializer import CustomerSerializer

from .serializer import OrderSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST'])
def customer_list(request):
    """
       Retrieve, update or delete .
       """

    if request.method == 'GET':
        articles = Customer.objects.all()
        serializer = CustomerSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'GET':
        customer = Order.objects.all()
        serializer = OrderSerializer(customer, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
