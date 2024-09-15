from django.shortcuts import render, redirect, reverse, get_object_or_404,\
    HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from services.models import Service
from cart.contexts import cart_contents
from accounts.forms import CustomUserCreationForm
from accounts.models import CustomUser

import stripe
# import json

# @require_POST
# def cache_checkout_data(request):
#     try:
#         pid = request.POST.get('client_secret').split('_secret')[0]
#         stripe.api_key = settings.STRIPE_SECRET_KEY
#         stripe.PaymentIntent.modify(pid, metadata={
#             'cart': json.dumps(request.session.get('cart', {})),
#             'save_info': request.POST.get('save_info'),
#             'username': request.user,
#         })
#         return HttpResponse(status=200)
#     except Exception as e:
#         messages.error(request, 'Sorry, your payment cannot be \
#             processed right now. Please try again later.')
#         return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'eircode': request.POST['eircode'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()#commit=False)
    #         pid = request.POST.get('client_secret').split('_secret')[0]
    #         order.stripe_pid = pid
    #         order.original_cart = json.dumps(cart)
    #         order.save()
            for item_id, item_data in cart.items():
                # try:
                service = Service.objects.get(id=item_id)
                if isinstance(item_data, int):
                    order_line_item = OrderLineItem(
                        order=order,
                        service=service,
                        number=item_data,
                    )
                    order_line_item.save()
                else:
                    if 'surfaces' in item_data.keys():
                        if 'Driveway/Patio' in item_data\
                            ['surfaces'].keys():
                            for surface, number in item_data\
                                ['surfaces'].items():
                                if surface == 'Driveway/Patio':
                                    order_line_item = OrderLineItem(
                                        order=order,
                                        service=service,
                                        number=number,
                                        surface=surface,
                                    )
                                    order_line_item.save()
                                else:
                                    continue
                        if 'Bed/Planter' in item_data['surfaces'].keys():
                            surface = 'Bed/Planter'
                            for size, number in item_data['surfaces']\
                                [surface]['sizes'].items():
                                order_line_item = OrderLineItem(
                                    order=order,
                                    service=service,
                                    number=number,
                                    surface=surface,
                                    size=size,
                                )
                                order_line_item.save()
                    elif 'cuts' in item_data.keys():
                        for cuts in item_data['cuts'].keys():
                            for size, number in item_data['cuts'][cuts]\
                                ['sizes'].items():
                                order_line_item = OrderLineItem(
                                    order=order,
                                    service=service,
                                    cuts=cuts,
                                    number=number,
                                    size=size,
                                )
                                order_line_item.save()
                    else:
                        for size, number in item_data['sizes'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                service=service,
                                number=number,
                                size=size,
                            )
                            order_line_item.save()

                # except Service.DoesNotExist:
                #     messages.error(request, (
                #         "One of the services in your cart wasn't found in our "
                #         "database. Please call us for assistance!")
                #     )
                #     order.delete()
                #     return redirect(reverse('view_cart'))
            
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success',args=[order.order_number]
                ))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There's nothing in your cart at the\
                 moment.")
            return redirect(reverse('services'))

        current_cart = cart_contents(request)
        total = current_cart['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    #     if request.user.is_authenticated:
    #         try:
    #             profile = CustomUser.objects.get(user=request.user)
    #             order_form = OrderForm(initial={
    #                 'full_name': profile.user.get_full_name(),
    #                 'email': profile.user.email,
    #                 'phone_number': profile.default_phone_number,
    #                 'country': profile.default_country,
    #                 'town_or_city': profile.default_town_or_city,
    #                 'stree_address1': profile.default_street_address1,
    #                 'street_address2': profile.default_street_address2,
    #                 'county': profile.default_county,
    #             })
    #         except CustomUser.DoesNotExist:
    #                 order_form = OrderForm()
    #     else:
    #         order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you \
            forget to set it in your environment?')

    # Temporary Line:
    order_form = OrderForm()

    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """ Handle successful checkouts """


    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

#     if request.user.is_authenticated:
#         profile = CustomUser.objects.get(user=request.user)
#         order.user_profile = profile
#         order.save()

#         if save_info:
#             profile_data = {
#                 'default_phone_number': order.phone_number,
#                 'default_street_address1': order.street_address1,
#                 'default_street_address2': order.street_address2,
#                 'default_town_or_city': order.town_or_city,
#                 'default_county': order.county,
#                 'default_eircode': order.eircode,
#             }
#             user_profile_form = CustomUserCreationForm(profile_data, instance=profile)
#             if user_profile_form.is_valid():
#                 user_profile_form.save()

    messages.success(request, f'Order successfully processed! A confirmation\
         email will be sent to {order.email}.')
    
    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
