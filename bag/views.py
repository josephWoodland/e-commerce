from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """View the user bag
    Args:
        request (GET): Get request
    Return:
        bag.html
    """
    return render(request, 'bag/bag.html')
