from django.shortcuts import get_object_or_404
from services.models import Service


def cart_contents(request):
    """
    Processor to make cart items dictionary available across the
    website.
    """

    cart_items = []
    total = 0
    item_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            service = get_object_or_404(Service, pk=item_id)
            total += item_data * service.unit_price
            item_count += item_data
            cart_items.append({
                'item_id': item_id,
                'number': item_data,
                'service': service,
            })
        else:
            service = get_object_or_404(Service, pk=item_id)
            if 'surfaces' in item_data.keys():
                print("item_data['surfaces'].keys() IS", item_data['surfaces'].keys())
                if 'drive' in item_data['surfaces'].keys():

                    print('drive is in the above!') # Debugging comment

                    for surface, number in item_data['surfaces'].items():
                        if surface == 'drive':
                            print('For Loop 2:')
                            print('surface:', surface)
                            print('number:', number)
                            print('total is', total) # Debugging comment
                            total += number * service.unit_price
                            print('new total is', total) # Debugging comment
                            item_count += number
                            cart_items.append({
                                'item_id': item_id,
                                'number': item_data,
                                'service': service,
                                'surface': surface,
                            })
                        else:
                            # break
                            continue
                if 'bed' in item_data['surfaces'].keys():
                    for size, number in item_data['surfaces']['bed']['sizes'].items():
                        print('For Loop 3:')
                        print('total is', total) # Debugging comment
                        print('number is', number) # Debugging comment
                        print('service.unit_price is', service.unit_price) # Debugging comment
                        total += number * service.unit_price
                        print('new total is', total) # Debugging comment
                        item_count += number
                        cart_items.append({
                            'item_id': item_id,
                            'number': item_data,
                            'service': service,
                            'size': size,
                        })
            else:
                for size, number in item_data['sizes'].items():
                    total += number * service.unit_price
                    item_count += number
                    cart_items.append({
                        'item_id': item_id,
                        'number': item_data,
                        'service': service,
                        'size': size,
                    })
    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
    }

    return context