from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(unit_price, number):
    """
    Take in the unit price and numer of service and return the service.
    """

    return unit_price * number
