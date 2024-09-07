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

    number = int(request.POST.get('number'))
    redirect_url = request.POST.get('redirect_url')

    size = None
    acres = None
    tree = None
    surface = None
    
    if 'size' in request.POST:
        size = request.POST.get('size')
    
    if 'tree' in request.POST:
        tree = request.POST.get('tree')
    
    if 'surface' in request.POST:
        surface = request.POST.get('surface')

    cart = request.session.get('cart', {})
    print('cart is', cart)  # Debugging comment
    print('size is', size)  # Debugging comment
    print('surface is', surface) # Debugging comment

    if surface:
        if surface == 'bed':
            if item_id in list(cart.keys()):
                if surface in cart[item_id]['surfaces'].keys():
                # Add a bed/planter to a cart already containing a bed/planter
                    if size in cart[item_id]['surfaces'][surface]['sizes'].keys():
                        cart[item_id]['surfaces'][surface]['sizes'][size] += number
                    else:
                        cart[item_id]['surfaces'][surface]['sizes'][size] = number
                else:
                    cart[item_id]['surfaces'][surface] = {'sizes': {size: number}}

            else:
                # Add a bed/planter to an empty cart
                cart[item_id] = {'surfaces': {surface: {'sizes': {size: number}}}}
        else:
            if item_id in list(cart.keys()):
                # Add a driveway to a cart containing at least 1 bed/planter
                # if surface in list(cart[item_id]['surfaces'].keys())
                # Add a driveway to a cart containing a driveway
                print('-------------------------') # Debugging comment
                print('cart[item_id] is', cart[item_id]) # Debugging comment
                print("cart[item_id]['surfaces'] is", cart[item_id]['surfaces']) # Debugging comment
                print("cart[item_id]['surfaces'][surface] is", cart[item_id]['surfaces'][surface]) # Debugging comment
                print('-------------------------') # Debugging comment
                cart[item_id]['surfaces'][surface] += number
            else:
                # Add a driveway to empty cart
                cart[item_id] = {'surfaces': {surface: number}}
                print('-------------------------') # Debugging comment
                print('cart[item_id] is', cart[item_id]) # Debugging comment
                print("cart[item_id]['surfaces'] is", cart[item_id]['surfaces']) # Debugging comment
                print("cart[item_id]['surfaces'][surface] is", cart[item_id]['surfaces'][surface]) # Debugging comment
                print('-------------------------') # Debugging comment
        
    # This handles both the acres option and the normal sizes option
    elif size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['sizes'].keys():
                cart[item_id]['sizes'][size] += number
            else:
                cart[item_id]['sizes'][size] = number
        else:
            cart[item_id] = {'sizes': {size: number}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += number
        else:
            cart[item_id] = number
    
    request.session['cart'] = cart
    print('cart is', cart) # Debugging comment
    return redirect(redirect_url)