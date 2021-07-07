from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# Views go here.
def index(request):
  products = Product.objects.all()
  return render(request, 'index.html', {'products': products})


def new(request):
  return HttpResponse('New Products')


#/product(url) -> index(fx) == mapping