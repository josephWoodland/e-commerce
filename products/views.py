from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.


def all_products(request):
    """View to show all products
        will handle searchs
    Args:
        request (GET): Get request
    Return:
        products.html
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """View to show a product
    Args:
        request (GET): Get request
        product_id (str): Product id
    Return:
        product<id>.html
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
