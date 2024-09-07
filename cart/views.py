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
    number = int(request.POST.get('number'))
    acres = request.POST.get('acres')
    tree = request.POST.get('tree')
    surface = request.POST.get('surface')
    redirect_url = request.POST.get('redirect_url')

    cart = request.session.get('cart', {})
    print('cart is', cart)
    # print('cart.keys() is', cart.keys())
    if item_id in list(cart.keys()):
        # print('item_id is', item_id)
        cart[item_id] += number
        # if item_id == '1':
            # cart[item_id] += acres
        # cart[item_id] += size
        # cart[item_id] += acres
        # cart[item_id] += tree
        # cart[item_id] += surface
        # print('cart[item_id] is', cart[item_id])
    else:
        print('item_id is', item_id)
        # cart[item_id] = {acres, number}
        cart[item_id] = number
        # if item_id == '1':
            # cart[item_id] += acres
        # print('cart[item_id] is', cart[item_id])
    
    request.session['cart'] = cart
    print('cart is', cart)
    return redirect(redirect_url)