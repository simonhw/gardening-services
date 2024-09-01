

def cart_contents(request):
    """
    Processor to make cart items dictionary available across the
    website.
    """

    cart_items = []
    total = 0
    item_count = 0

    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
    }

    return context