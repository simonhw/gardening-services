from django.shortcuts import render, redirect


def view_cart(request):
    ''' View that renders the shopping cart page '''

    return render(
        request,
        "cart/cart.html"
    )


def add_to_cart(request, item_id):
    """
    Add the service to the shopping cart with its relevant options
    """

    size = request.POST.get('size')
    number = request.POST.get('number')
    acres = request.POST.get('acres')
    tree = request.POST.get('tree')
    surface = request.POST.get('surface')
    redirect_url = request.POST.get('redirect_url')

    cart = request.session.get('cart', {})
    if item_id in list(cart.keys()):
        cart[item_id] += int(number)
        # if item_id == '1':
            # cart[item_id] += acres
        # cart[item_id] += size
        # cart[item_id] += acres
        # cart[item_id] += tree
        # cart[item_id] += surface
    else:
        cart[item_id] = int(number)
        # if item_id == '1':
            # cart[item_id] += acres
    
    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)