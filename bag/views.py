from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')
<<<<<<< HEAD


def add_to_bag(request, item_id):
    """Add an item to a shopping bag

    Args:
        request (HTTP): POST request to the server
        item_id (str): item id string
    """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print('Session: ', request.session['bag'])
    return redirect(redirect_url)
=======
>>>>>>> parent of db96be3 (Add to bag functionlity)
