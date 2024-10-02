import uuid

from django.db import models
from django.db.models import Sum

from services.models import Service
from accounts.models import UserAccount


class Order(models.Model):
    """
    A model for user orders.

    Fields:
        order_number - A unique number for each order
        user_account - The user who places the order
        full_name - The user's name
        email - Email associated with the order
        phone_number - Phone number associated with the order
        street_address1 - Required address field
        street_address2 - Optional address field
        town_or_city - Required address field
        county - Required address field
        eircode - Optional address field
        date - The date that the order is created
        grand_total - The total cose of the order
        original_cart - The dictionary of services that were ordered
        stripe_pid - The Stripe payment ID
        """

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_account = models.ForeignKey(
        UserAccount,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
        )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=False, blank=False)
    eircode = models.CharField(max_length=20, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
        )
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default=''
        )

    def _generate_order_number(self):
        """ Generate a random unique order number using UUID """

        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ Update grand total each time a line item is added """

        self.grand_total = self.lineitems.aggregate(
            Sum('lineitem_total')
            )['lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to generate a order
        number if it hasn't already been set.
        """

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    A model for individal service variations in an order.

    Fields:
        order (ForeignKey) - The order the service is a part of
        service (ForeignKey) - The service being added to the line
        surface (CharField) - To denote if the service has a surface
                              attribute
        cuts (CharField) - To denote if the service has a tree-related
                           attribute
        size (CharField) - To denote if the service has a size
                           attribute
        number (IntegerField) - To denote if the service has a number
                                attribute
        line_item_total (DecimalField) - The subtotal for the line
    """

    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems'
    )
    service = models.ForeignKey(
        Service, null=False, blank=False, on_delete=models.CASCADE
    )
    surface = models.CharField(max_length=14, null=True, blank=True)
    cuts = models.CharField(max_length=10, null=True, blank=True)
    size = models.CharField(max_length=14, null=True, blank=True)
    number = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total and
        update the order total.
        """

        self.lineitem_total = self.service.unit_price * self.number
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.service.name} on order {self.order.order_number}'
