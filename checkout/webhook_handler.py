from django.http import HttpResponse
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from django.conf import settings
from .models import Order, OrderLineItem
from services.models import Service
# from accounts.models import CustomUser

import stripe

import json
import time


class StripeWH_Handler:
    """ Webhook handler for Stripe payments """

    def __init__(self, request):
        self.request = request
    

#     def _send_confirmation_email(self, order):
#         """ Send the user a confirmation email. """

#         cust_email = order.email
#         subject = render_to_string(
#             'checkout/confirmation_emails/confirmation_email_subject.txt',
#             {'order': order}
#         )
#         body = render_to_string(
#             'checkout/confirmation_emails/confirmation_email_body.txt',
#             {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
#         )
#         send_mail(
#             subject,
#             body,
#             settings.DEFAULT_FROM_EMAIL,
#             [cust_email]
#         )

    def handle_event(self, event):
        """ Handle a generic/unknown/unexpected webhook event """

        return HttpResponse(
            content = f'Unhandled webhook received: {event['type']}',
            status = 200
        )
    

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment intent succeeded webhook event from Stripe
        """

        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details # updated
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2) # updated

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == '':
                shipping_details.address[field] = None

#         profile = None
#         username = intent.metadata.username
#         if username != 'AnonymousUser':
#             profile = UserProfile.objects.get(user__username=username)
#             if save_info:
#                 profile.default_phone_number = shipping_details.phone
#                 profile.default_country = shipping_details.address.country
#                 profile.default_postcode = shipping_details.address.postal_code
#                 profile.default_town_or_city = shipping_details.address.city
#                 profile.default_street_address1 = shipping_details.address.line1
#                 profile.default_street_address2 = shipping_details.address.line2
#                 profile.default_county = shipping_details.address.state
#                 profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact = shipping_details.name,
                    email__iexact = billing_details.email,
                    phone_number__iexact = shipping_details.phone,
                    street_address1__iexact = shipping_details.address.line1,
                    street_address2__iexact = shipping_details.address.line2,
                    town_or_city__iexact = shipping_details.address.city,
                    county__iexact = shipping_details.address.state,
                    eircode__iexact = shipping_details.address.postal_code,
                    grand_total = grand_total,
                    original_cart = cart,
                    stripe_pid = pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if  order_exists:
#             self._send_confirmation_email(order)
            return HttpResponse(
                    content = f'Webhook received: {event['type']} |\
                         SUCCESS: Verified order already in database.',
                    status = 200
                    )
        else:
            order = None
            try:
                order = Order.objects.create(
                        full_name = shipping_details.name,
                        # user_profile=profile,
                        email = billing_details.email,
                        phone_number = shipping_details.phone,
                        street_address1 = shipping_details.address.line1,
                        street_address2 = shipping_details.address.line2,
                        town_or_city = shipping_details.address.city,
                        county = shipping_details.address.state,
                        eircode = shipping_details.address.postal_code,
                        original_cart = cart,
                        stripe_pid = pid,
                    )
                
                for item_id, item_data in json.loads(cart).items():
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
                                for size, number in item_data\
                                    ['cuts'][cuts]['sizes'].items():
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
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content = f'Webhook received: {event['type']} |\
                        ERROR: {e}', status = 500
                )
                            
#         self._send_confirmation_email(order)
        
        return HttpResponse(
                content = f'Webhook received: {event['type']} | SUCCESS: \
                    Created order in webhook handler',
                status = 200
            )


    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment intent payment failed webhook event from
        Stripe
        """

        return HttpResponse(
            content = f'Webhook received: {event['type']}',
            status = 200
        )