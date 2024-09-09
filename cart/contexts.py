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
                if 'Driveway/Patio' in item_data['surfaces'].keys():
                    for surface, number in item_data['surfaces'].items():
                        if surface == 'Driveway/Patio':
                            total += number * service.unit_price
                            item_count += number
                            cart_items.append({
                                'item_id': item_id,
                                'number': number,
                                'service': service,
                                'surface': surface,
                            })
                        else:
                            continue
                if 'Bed/Planter' in item_data['surfaces'].keys():
                    surface = 'Bed/Planter'
                    for size, number in item_data['surfaces'][surface]\
                        ['sizes'].items():
                        total += number * service.unit_price
                        item_count += number
                        cart_items.append({
                            'item_id': item_id,
                            'number': number,
                            'service': service,
                            'surface': surface,
                            'size': size,
                        })
            elif 'cuts' in item_data.keys():
                for cuts in item_data['cuts'].keys():
                    for size, number in item_data['cuts'][cuts]\
                        ['sizes'].items():
                        total += number * service.unit_price
                        item_count += number
                        cart_items.append({
                            'item_id': item_id,
                            'number': number,
                            'service': service,
                            'size': size,
                            'cuts': cuts,
                        })

            else:
                for size, number in item_data['sizes'].items():
                    total += number * service.unit_price
                    item_count += number
                    cart_items.append({
                        'item_id': item_id,
                        'number': number,
                        'service': service,
                        'size': size,
                    })
    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
    }

    return context