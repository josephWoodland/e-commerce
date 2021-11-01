from django.shortcuts import render
from .models import Product
# Create your views here.


def all_products(request):
    """View to show al products
        will handle searchs
    Args:
        request (GET): Get request
    Return:
        products.html
    """

    products = Product.object.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)
