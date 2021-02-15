from django.urls import path, include
from .views import order_list
from .views import customer_list
from django.conf.urls import url


urlpatterns = [
    path('order/', order_list),
    path('customer/', customer_list),

    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

]

