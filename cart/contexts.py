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

                print("item_data['surfaces'].keys() is", item_data['surfaces'].keys()) # Debugging comment
                # print("item_data['surfaces']['drive'] is", item_data['surfaces']['drive']) # Debugging comment

                for surface in item_data['surfaces'].items():
                    print('For Loop 1:')
                    print('surface:', surface)

                    if 'drive' in item_data['surfaces'].keys():

                        print('drive is in the above!') # Debugging comment

                        for surface, number in item_data['surfaces'].items():
                            if surface == 'drive':
                                print('For Loop 2:')
                                print('surface:', surface)
                                print('number:', number)
                                total += number * service.unit_price
                                item_count += number
                                cart_items.append({
                                    'item_id': item_id,
                                    'number': item_data,
                                    'service': service,
                                    'surface': surface,
                                })
                            else:
                                break
                    if 'bed' in item_data['surfaces'].keys():
                        for size, number in item_data['surfaces']['bed']['sizes'].items():
                            total += number * service.unit_price
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