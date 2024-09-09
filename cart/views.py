from django.shortcuts import render, redirect, reverse, HttpResponse, \
    get_object_or_404
from django.contrib import messages
from services.models import Service


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

    service = get_object_or_404(Service, pk=item_id)
    number = int(request.POST.get('number'))
    redirect_url = request.POST.get('redirect_url')

    size = None
    tree = None
    surface = None
    
    if 'size' in request.POST:
        size = request.POST.get('size')
    if 'tree' in request.POST:
        tree = request.POST.get('tree')
    if 'surface' in request.POST:
        surface = request.POST.get('surface')

    cart = request.session.get('cart', {})

    if surface:
        if surface == 'Bed/Planter':
            # If block for a cart already containing a Weeding service
            if item_id in list(cart.keys()):
                if surface in cart[item_id]['surfaces'].keys():
                    # When there is already a Bed/Planter service in
                    #  the cart, check if there is one of the same size
                    #  and increment the number if so, otherwise add
                    #  the new size. 
                    if size in cart[item_id]['surfaces'][surface]\
                        ['sizes'].keys():
                        cart[item_id]['surfaces'][surface]\
                            ['sizes'][size] += number
                        messages.success(
                            request, f'{service.name}: added {number} {size}\
                                    {surface} to cart'
                        )
                    else:
                        cart[item_id]['surfaces'][surface]\
                            ['sizes'][size] = number
                        messages.success(
                            request, f'{service.name}: added {number} {size}\
                                    {surface} to cart'
                        )
                else:
                    # In this case, there is a Driveway/Patio service
                    #  in the cart and no Bed/Planter service.
                    #  Therefore, create a new Bed/Planter dictionary.
                    cart[item_id]['surfaces'][surface] = \
                        {'sizes': {size: number}}
                    messages.success(
                        request, f'{service.name}: added {number} {size}\
                                {surface} to cart'
                    )

            else:
                # There is no Weeding service already in the cart.
                #  Create a new dictionary.
                cart[item_id] = {'surfaces':\
                     {surface: {'sizes': {size: number}}}}
                messages.success(
                    request, f'Added {service.name}:\
                            {size} {surface} x{number} to cart'
                )
        else:
            # When the service is a Driveway/Patio, check if the cart
            #  already contains Weeding services. If it does and a
            #  Driveway/Patio is already present, increment the number.
            #  If it does not, add a new dictionary.
            if item_id in list(cart.keys()):
                if surface in cart[item_id]['surfaces'].keys():
                    cart[item_id]['surfaces'][surface] += number
                    messages.success(
                        request, f'Added {service.name}:\
                            {surface} x{number} to cart'
                    ) 
                else:
                    cart[item_id]['surfaces'][surface] = number
                    messages.success(
                        request, f'Added {service.name}:\
                            {surface} x{number} to cart'
                    ) 
            else:
                # There is no Weeding service already in the cart.
                #  Create a new dictionary.
                cart[item_id] = {'surfaces': {surface: number}}
                messages.success(
                    request, f'Added {service.name}:\
                         {surface} x{number} to cart'
                )    
    elif tree:
        # For carts where there is already a Tree Maintenance service,
        #  check if the specific tree service already has a dictionary
        #  in the cart with the same size tree. If so, increment the
        #  number, otherwise add the new size.
        if item_id in list(cart.keys()):
            if tree in cart[item_id]['cuts'].keys():
                if size in cart[item_id]['cuts'][tree]['sizes'].keys():
                    cart[item_id]['cuts'][tree]['sizes'][size] += number
                    messages.success(
                        request, f'Added {size.title()} Tree {tree.title()}\
                            to cart ({number})'
                    )
                else:
                    cart[item_id]['cuts'][tree]['sizes'][size] = number
                    messages.success(
                        request, f'Added {size.title()} Tree {tree.title()}\
                            to cart ({number})'
                    )
            else:
                # If the specific tree service isn't already present in
                #  the cart, create a new dictionary.
                cart[item_id]['cuts'][tree] = {'sizes': {size: number}}
                messages.success(
                    request, f'Added {size.title()} Tree {tree.title()}\
                         to cart ({number})'
                )

        else:
            # Where is no Tree Maintenance service in the cart yet,
            #  create a new dictionary.
            cart[item_id] = {'cuts': {tree: {'sizes': {size: number}}}}
            messages.success(
                request, f'Added {number} {size.title()}\
                        Tree {tree.title()} to cart'
            )
    # This handles both the acres option and the normal sizes option
    elif size:
        # For carts already containing the service that only has size
        #  options, check if the specific size is present. If so,
        #  increment the number, otherwise add a new dictionary.
        if item_id in list(cart.keys()):
            if size in cart[item_id]['sizes'].keys():
                cart[item_id]['sizes'][size] += number
                messages.success(
                    request, f'Added {service.name}: {size} x{number} to cart'
                )
            else:
                cart[item_id]['sizes'][size] = number
                messages.success(
                    request, f'Added {service.name}: {size} x{number} to cart'
                )
        else:
            # If the service does not exist in the cart yet, create a
            #  new dictionary.
            cart[item_id] = {'sizes': {size: number}}
            messages.success(
                request, f'Added {service.name}: {size} x{number} to cart'
            )
    else:
        # For services that only take a number input, check if the
        #  service is already listed in the cart. Increment the number
        #  if so, otherwise add a new dictionary.
        if item_id in list(cart.keys()):
            cart[item_id] += number
            messages.success(
                request, f'Added {service.name} x{number} to cart.'
            )
        else:
            cart[item_id] = number
            messages.success(
                request, f'Added {service.name} x{number} to cart.'
            )
    
    request.session['cart'] = cart
    return redirect(redirect_url)


def amend_cart(request, item_id):
    """ Update or amend the services currently in the shopping cart """

    service = get_object_or_404(Service, pk=item_id)
    number = int(request.POST.get('number'))

    size = None
    tree = None
    surface = None
    
    if 'size' in request.POST:
        size = request.POST.get('size')
    if 'cuts' in request.POST:
        tree = request.POST.get('cuts')
    if 'surface' in request.POST:
        surface = request.POST.get('surface')

    cart = request.session.get('cart', {})

    if surface:
        if surface == 'Bed/Planter':
            if number > 0:
                # Update the number of the specific size Bed/Planter
                cart[item_id]['surfaces'][surface]['sizes'][size] = number
                messages.success(
                    request, f'Updated {service.name}:\
                            {size} {surface} to {number}'
                )
            else:
                # Delete the entry if the specified number is 0 and
                #  remove the parent dictionary if it is empty.
                del cart[item_id]['surfaces'][surface]['sizes'][size]
                messages.success(
                    request, f'Removed {service.name}:\
                            {size} {surface} from cart.'
                )
                if not cart[item_id]['surfaces']:
                    cart.pop(item_id)
        else:
            if number > 0:
                # Update the number of the specific size Driveway/Patio
                cart[item_id]['surfaces'][surface] = number
                messages.success(
                    request, f'Updated {service.name}: {surface} to {number}'
                )
            else:
                # Delete the entry if the specified number is 0 and
                #  remove the parent dictionary if it is empty.
                del cart[item_id]['surfaces'][surface]
                messages.success(
                    request, f'Removed {service.name}: {surface} from cart.'
                )
                if not cart[item_id]['surfaces']:
                    cart.pop(item_id)
    elif tree:
        if number > 0:
            # Update the number of the specific size tree service
            cart[item_id]['cuts'][tree]['sizes'][size] = number
            messages.success(
                request, f'Updated {service.name}:\
                    {size} tree {tree} to {number}'
            )
        else:
            # Delete the entry if the specified number is 0 and
            #  remove the parent dictionary if it is empty.
            del cart[item_id]['cuts'][tree]['sizes'][size]
            messages.success(
                request, f'Removed {service.name}:\
                    {size} tree {tree} from cart.'
            )
            if not cart[item_id]['cuts']:
                cart.pop(item_id)
    elif size:
        if number > 0:
            # Update the number of the specific size service
            cart[item_id]['sizes'][size] = number
            messages.success(
                request, f'Updated {service.name}: {size} to {number}'
            )
        else:
            # Delete the entry if the specified number is 0 and
            #  remove the parent dictionary if it is empty.
            del cart[item_id]['sizes'][size]
            messages.success(
                request, f'Removed {service.name}: {size} from cart'
            )
            if not cart[item_id]['sizes']:
                cart.pop(item_id)
    else:
        if number > 0:
            # Update the number of the specific service
            cart[item_id] = number
            messages.success(
                request, f'Updated {service.name} to {number}'
            )
        else:
            # Delete the entry if the specified number is 0
            cart.pop(item_id)
            messages.success(
                request, f'Removed {service.name} from cart'
            )
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Delete services currently in the shopping cart """

    service = get_object_or_404(Service, pk=item_id)

    try:
        size = None
        tree = None
        surface = None
        
        if 'size' in request.POST:
            size = request.POST.get('size')
        if 'cuts' in request.POST:
            tree = request.POST.get('cuts')
        if 'surface' in request.POST:
            surface = request.POST.get('surface')

        cart = request.session.get('cart', {})

        if surface:
            if surface == 'Bed/Planter':
                # Delete the specific size of Bed/Planter only
                del cart[item_id]['surfaces'][surface]['sizes'][size]
                messages.success(
                    request, f'Removed {service.name}:\
                            {size} {surface} from cart.'
                )
                if not cart[item_id]['surfaces'][surface]['sizes']:
                    # Delete an empty Bed/Planter dictionary
                    del cart[item_id]['surfaces'][surface]
            else:
                # Delete the Driveway/Patio dictionary
                del cart[item_id]['surfaces'][surface]
                messages.success(
                    request, f'Removed {service.name}: {surface} from cart.'
                )
            if not cart[item_id]['surfaces']:
                # If the Weeding dictionary contains empty
                #  dictionaries, remove it from the cart
                cart.pop(item_id)
        elif tree:
            # Delete the specific size of tree service, then check if
            #  any other sizes exists. If they don't delete the
            #  specific tree service. 
            del cart[item_id]['cuts'][tree]['sizes'][size]
            if not cart[item_id]['cuts'][tree]['sizes']:
                del cart[item_id]['cuts'][tree]
                if not cart[item_id]['cuts']:
                    # If the Tree Maintenance dictionary contains empty
                    #  dictionaries, remove it from the cart
                    cart.pop(item_id)
            messages.success(
                request, f'Removed {service.name}:\
                    {size} tree {tree} from cart.'
            )
        elif size:
            # Delete a specific size of sized service
            del cart[item_id]['sizes'][size]
            messages.success(
                request, f'Removed {service.name}: {size} from cart'
            )
            if not cart[item_id]['sizes']:
                # If the specific service has no other sizes present in
                #  the cart, remove it
                cart.pop(item_id)
        else:
            # Remove a number-only service
            cart.pop(item_id)
            messages.success(request, f'Removed {service.name} from cart')
            
        
        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)