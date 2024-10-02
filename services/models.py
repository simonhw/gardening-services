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
    A custom Service model for the gardening services on offer

    Fields:
        category (ForeignKey) - The category type of the service
        name (CharField) - The name of the service
        unit_price (DecimalField) - The minimum price of the service
                                    based on how it is carried out
        description (TextField) - A full description of the service
        image (URLField) - An image representing the service
        alt (CharField) - Image alt test for accessibility
        review_count (PositiveIntegerField) - The number of published
                                              reviews a service has
        average_rating (DecimalField) - The average value of all the
                                        published review ratings a 
                                        service has 
        has_sizes (BooleanField) - Denotes whether or not the service
                                   can have the size attribute
        has_acres (BooleanField) - Denotes whether or not the service
                                   can have the acre attribute
        has_fellprune (BooleanField) - Denotes whether or not the
                                       service can have the 
                                       tree-related attribute
        has_surface (BooleanField - Denotes whether or not the service
                                    can have the surface attribute
    """

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
        )
    name = models.CharField(max_length=254)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    alt = models.CharField(null=True, max_length=254)
    review_count = models.PositiveIntegerField(null=True, blank=True)
    average_rating = models.DecimalField(
                                 max_digits=2, decimal_places=1,
                                 null=True, blank=True
                                 )
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    has_acres = models.BooleanField(default=False, null=True, blank=True)
    has_fellprune = models.BooleanField(default=False, null=True, blank=True)
    has_surface = models.BooleanField(default=False, null=True, blank=True)

    def calculate_average_rating(self):
        """
        Method that loops through all approved reviews for the service
        and sums their ratings and divides by the total number of 
        approved reviews to get an average value.
        """

        reviews = self.reviews.filter(approved=True)
        if reviews:
            summed_ratings = sum(review.rating for review in reviews)
            self.average_rating = summed_ratings / reviews.count()
            self.review_count = reviews.count()
            self.save()

    def __str__(self):
        return self.name
