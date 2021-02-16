I am creating Rest API using django-rest-framework


The first step is setting up an environment for my project using Pycharm IDE


Getting started
 let's create a new project to work with using this command in the terminal
      django-admin startproject myproject
      cd myproject

Once that's done we can create an app that we'll use to create a simple Web API.

python manage.py startapp E_shop

We'll need to add our new E_shop app and the rest_framework app to INSTALLED_APPS. Let's edit the myproject/settings.py file:

INSTALLED_APPS = [
  
    'rest_framework',
    'E_shop',
]

We will now create a model to work with

 Go ahead and edit the E_shop/models.py

from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


# Create your models here.
class Customer(models.Model):
    Name = models.CharField(max_length=50)
    Code = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def _def_(self):
        return self.title


class Order(models.Model):
    item = models.CharField(max_length=50)
    amount = models.CharField(max_length=100)
    date = models.TimeField(auto_now_add=True)

    def _def_(self):
        return self.title

We'll also need to create an initial migration for our Customer
 and Order model, and sync the database for the first time.


python manage.py makemigrations snippets
python manage.py migrate



Creating a Serializer class

The first thing we need to get started on our Web API is to provide
 a way of serializing and deserializing the customer and order instances into 
representations such as json. We can do this by declaring serializers
 that work very similar to Django's forms. Create a file in the snippets 
directory named serializers.py and add the following.

from rest_framework import serializers
from .models import Customer
from .models import Order
from django.contrib.auth.models import User




class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'Name', 'Code', 'email']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'item', 'amount', 'date']


Writing Django views using our Serializer

from .models import Customer
from .models import Order
from .serializer import CustomerSerializer

from .serializer import OrderSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST'])
def customer_list(request):
    """
       Retrieve, add  .
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

lets now create urls.py in E_shop application then make the following changes in project urls.py files


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('E_shop.urls'))
]

Then edit the urls.py file you just created as follows

from django.urls import path
from .views import order_list
from .views import customer_list
from django.conf.urls import url


urlpatterns = [
    path('order/', order_list),
    path('customer/', customer_list),

Testing our first attempt at a Web API
python manage.py runserver

Now we want to make your own Authorization Server to issue access tokens to client applications for API.

 We will need to install the django-cors-middleware app 
 cross-domain requests are by default forbidden by web browsers unless you use CORS.

pip install django-oauth-toolkit django-cors-middleware

add oauth2_provider and corsheaders to the installed apps, and enable admin:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'E_shop',
    'oauth2_provider',
]

Include the Django OAuth Toolkit urls in your urls.py


urlpatterns = [
    path('order/', order_list),
    path('customer/', customer_list),

    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

]

Include the CORS middleware in your settings.py:
CorsMiddleware should be placed as high as possible, especially before any middleware 
that can generate responses such as Django’s CommonMiddleware 
or Whitenoise’s WhiteNoiseMiddleware. If it is not before, 
it will not be able to to add the CORS headers to these responses.

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]
