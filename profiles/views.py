from django.shortcuts import render

# Create your views here.


def profile(request):
    """Displays the user's profile

    Args:
        request (HTTP request): Direct to the users profile page
    """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
