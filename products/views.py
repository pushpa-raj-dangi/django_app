from math import remainder
from django.shortcuts import render
from django.http import HttpResponse

from products.models import Product

# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new_product(request):

    return render(request, 'new.html')


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'detail.html', {'product': product})
