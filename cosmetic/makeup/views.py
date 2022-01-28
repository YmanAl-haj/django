from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request,'makeup/index.html')

def brand(request):

    return render(request,'makeup/brand.html')

def product(request):

    return render(request,'makeup/product.html')