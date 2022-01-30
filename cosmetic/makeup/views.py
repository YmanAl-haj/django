from django.shortcuts import render
from .models import Brand,Products
from django.db.models import Count
# Create your views here.

def index(request):
    """
        this is index page
    """
    context = {}
    try:
        brandi=Brand.objects.all().annotate(num_products=Count('products'))
        # brandi = Products.objects.all().values('brand').annotate(total=Count('brand')) #.order_by('brand').
        context['brandi'] = brandi
    except Products.DoesNotExist:
        context['error'] = 'Not Found'

    template_name='makeup/index.html'
    return render(request,template_name,context)

def brand(request):
    """
        this is brand page
    """
    context={}
    try:
        brand=Brand.objects.all()
        context['brand']=brand
    except Brand.DoesNotExist:
        context['error']='Not Found'
    template_name = 'makeup/brand.html'

    return render(request,template_name,context)

def product(request):
    """
        this is Product page
    """
    context = {}
    try:
        product = Products.objects.all()
        context['product'] = product
    except Brand.DoesNotExist:
        context['error'] = 'Not Found'
    template_name = 'makeup/product.html'
    return render(request,template_name,context)


def prodetails(request,id):
    """
        this is Product details page
    """
    context = {}
    try:
        productd = Products.objects.get(id=id)
        context['productd'] = productd
    except Products.DoesNotExist:
        context['error'] = "Not Found"

    template_name = 'makeup/prodetails.html'
    return render(request,template_name,context)

def branddetails(request,name):
    """
        this is Brand details page
    """
    context = {}
    try:
        # brandd=Products.objects.select_related(name).all()
        brandd=Products.objects.filter(brand__name__exact=name)
        context['brandd'] = brandd
    except Products.DoesNotExist:
        context['error'] = "Not Found"

    template_name = 'makeup/branddetails.html'
    return render(request,template_name,context)
