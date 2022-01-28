from django.urls import path
from makeup.views import index,brand,product


urlpatterns=[
    path('index',index,name='index'),
    path('brand',brand,name='brand'),
    path('product',product,name='product'),
]