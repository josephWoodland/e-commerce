from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
# Create your views here.


def profile(request):
    """Displays the user's profile

    Args:
        request (HTTP request): Direct to the users profile page
    """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':

        form = UserProfile(request.POST, instance=profile)

        if form.is_vaild():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'order': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)
