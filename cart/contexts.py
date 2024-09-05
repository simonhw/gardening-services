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

    for item_id, number in cart.items():
        service = get_object_or_404(Service, pk=item_id)
        total += number * service.unit_price
        item_count += number
        cart_items.append({
            'item_id': item_id,
            'number': number,
            'service': service,
        })
    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
    }

    return context