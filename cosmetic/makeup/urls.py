from django.urls import path,re_path
from makeup.views import index,brand,product,prodetails,branddetails,updateItem,cart

urlpatterns=[
    path('',index,name='index'),
    path('brand',brand,name='brand'),
    path('product',product,name='product'),
    path('prodetails/<int:id>',prodetails,name='prodetails'),
    path('branddetails/<str:name>',branddetails,name='branddetails'),
    path('updateItem/',updateItem,name='updateItem'),
    path('cart/',cart,name='cart'),


]