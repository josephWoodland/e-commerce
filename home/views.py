from django.shortcuts import render

# Create your views here.


def index(request):
    """View
    Args:
        request (GET): Get request
    Return:
        index.html
    """
    return render(request, 'home/index.html')
