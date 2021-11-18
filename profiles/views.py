from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
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


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        (f'This is a past conformation for order number {order_number}.'
         'A conformation email was sent on the order date.'))

    template = 'checkout/checkout_success.html'
    context = {'order': order, 'from_profile': True}

    return render(request, template, context)
