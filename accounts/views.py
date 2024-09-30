from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserAccount
from checkout.models import Order

from .forms import UserAccountForm


def account(request):
    """ Display the user's account page """

    account = get_object_or_404(UserAccount, user=request.user)

    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully updated')

    form = UserAccountForm(instance=account)
    orders = account.orders.all()

    template = 'accounts/account.html'
    context = {
        'form': form,
        'orders': orders,
        'on_account_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ Display a past order confirmation to the user """

    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        'This is a past confirmation for this order. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_account': True,
    }

    return render(request, template, context)


def privacy_policy(request):
    """ View that renders the privacy policy page """

    return render(
        request,
        "accounts/privacy.html"
    )
