from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages


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
    print('number in request.POST:', 'number' in request.POST)
    redirect_url = request.POST.get('redirect_url')

    size = None
    tree = None
    surface = None
    
    if 'size' in request.POST:
        print("'size' in request.POST")
        size = request.POST.get('size')
    
    if 'tree' in request.POST:
        print("'tree' in request.POST")
        tree = request.POST.get('tree')
    
    if 'surface' in request.POST:
        print("'surface' in request.POST")
        surface = request.POST.get('surface')

    cart = request.session.get('cart', {})

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
                if surface in cart[item_id]['surfaces'].keys():
                    # Add a driveway to a cart containing a driveway
                    cart[item_id]['surfaces'][surface] += number
                else:
                    # Add a driveway to a cart containing at least 1 bed/planter
                    cart[item_id]['surfaces'][surface] = number
            else:
                # Add a driveway to empty cart
                cart[item_id] = {'surfaces': {surface: number}}
    
    elif tree:
        if item_id in list(cart.keys()):
            if tree in cart[item_id]['cuts'].keys():
                if size in cart[item_id]['cuts'][tree]['sizes'].keys():
                    cart[item_id]['cuts'][tree]['sizes'][size] += number
                else:
                    cart[item_id]['cuts'][tree]['sizes'][size] = number
            else:
                cart[item_id]['cuts'][tree] = {'sizes': {size: number}}

        else:
            cart[item_id] = {'cuts': {tree: {'sizes': {size: number}}}}
    
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
    print(cart)

    return redirect(redirect_url)


def amend_cart(request, item_id):
    """ Update or amend the services currently in the shopping cart """

    number = int(request.POST.get('number'))
    print('request is', request)
    print('number in request.POST:', 'number' in request.POST)

    size = None
    tree = None
    surface = None
    
    print('request.POST is', request.POST)
    if 'size' in request.POST:
        print("'size' in request.POST")
        size = request.POST.get('size')
    
    if 'tree' in request.POST:
        print("'tree' in request.POST")
        tree = request.POST.get('tree')
    
    if 'surface' in request.POST:
        print("'surface' in request.POST")
        surface = request.POST.get('surface')

    cart = request.session.get('cart', {})

    if surface:
        if surface == 'bed':
            print('line 1')
            if number > 0:
                cart[item_id]['surfaces'][surface]['sizes'][size] = number
                print('line 2')
            else:
                del cart[item_id]['surfaces'][surface]['sizes'][size]
                print('line 3')
                if not cart[item_id]['surfaces']:
                    cart.pop(item_id)
                    print('line 4')
        else:
            if number > 0:
                cart[item_id]['surfaces'][surface] = number
                print('line 5')
            else:
                del cart[item_id]['surfaces'][surface]
                print('line 6')
                if not cart[item_id]['surfaces']:
                    cart.pop(item_id)
                    print('line 7')

    elif tree:
        if number > 0:
            cart[item_id]['cuts'][tree]['sizes'][size] = number
            print('line 8')
        else:
            del cart[item_id]['cuts'][tree]['sizes'][size]
            print('line 9')
            if not cart[item_id]['cuts']:
                cart.pop(item_id)
                print('line 10')
    elif size:
        if number > 0:
            cart[item_id]['sizes'][size] = number
            print('line 11')
        else:
            del cart[item_id]['sizes'][size]
            print('line 12')
            if not cart[item_id]['sizes']:
                cart.pop(item_id)
                print('line 13')
    else:
        if number > 0:
            cart[item_id] = number
            print('line 14')
        else:
            cart.pop(item_id)
            print('line 15')
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Delete services currently in the shopping cart """

    # try:
    size = None
    tree = None
    surface = None
    
    if 'size' in request.POST:
        print("'size' in request.POST")
        size = request.POST.get('size')
    
    if 'cuts' in request.POST:
        print("'cuts' in request.POST")
        tree = request.POST.get('cuts')
    
    if 'surface' in request.POST:
        print("'surface' in request.POST")
        surface = request.POST.get('surface')

    cart = request.session.get('cart', {})

    if surface:
        if surface == 'bed':
            del cart[item_id]['surfaces'][surface]['sizes'][size]
            print('line 20')
            if not cart[item_id]['surfaces'][surface]['sizes']:
                del cart[item_id]['surfaces'][surface]
                print('line 20.5')
        else:
            del cart[item_id]['surfaces'][surface]
            print('line 21')
        if not cart[item_id]['surfaces']:
            cart.pop(item_id)
            print('line 22')
    elif tree:
        del cart[item_id]['cuts'][tree]['sizes'][size]
        print('line 22')
        if not cart[item_id]['cuts'][tree]['sizes']:
            del cart[item_id]['cuts'][tree]
            print('line 23')
            if not cart[item_id]['cuts']:
                cart.pop(item_id)
    elif size:
        del cart[item_id]['sizes'][size]
        print('line 24')
        if not cart[item_id]['sizes']:
            cart.pop(item_id)
            print('line 25')
    else:
        cart.pop(item_id)
        print('line 26')
    
    request.session['cart'] = cart
    print(cart)
    return HttpResponse(status=200)
    # except Exception as e:
    #     messages.error(request, f'Error removing item: {e}')
    #     return HttpResponse(status=500)