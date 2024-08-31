from django.db import models

class Category(models.Model):
    """
    Gives a specific category for each service. Model taken from the 
    Boutique Ado walkthrough.
    """
    
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Service(models.Model):
    """
    Model for the gardening services on offer.

    Fields:
        category (ForeignKey) - The category type of the service
        name (CharField) - The name of the service
        image (URLField) - An image representing the service
        unit_price (DecimalField) - The minimum price of the service
                                    based on how it is carried out
        description (TextField - A full description of the service
        rating (DecimalField) - A rating of the service based on
                                customer reviews
    """

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
        )
    name = models.CharField(max_length=254)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name