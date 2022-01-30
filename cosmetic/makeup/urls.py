from django.urls import path,re_path
from makeup.views import index,brand,product,prodetails,branddetails
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path('index',index,name='index'),
    path('brand',brand,name='brand'),
    path('product',product,name='product'),
    path('prodetails/<int:id>',prodetails,name='prodetails'),
    path('branddetails/<str:name>',branddetails,name='branddetails'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)