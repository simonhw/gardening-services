from django.db import models
from accounts.models import CustomUser
from services.models import Service


class Review(models.Model):
    """
    A custom model for service Reviews.

    Fields:
        reviewer (ForeignKey) - A foreign key linked to the
                                authenticated user
        service (ForeignKey) - The service being reviewed
        title (CharField) - A review title
        content (CharField) - The body of the review text
        created_on (DateField) - The date that the review was
                                 originally submitted
        updated_on (DateField) - The date that the review was last
                                 edited or published
        approved (BooleanField) - Denotes if the review has been
                                  published or not
        rating (IntegerField) - The user's rating from 1 to 5
    """

    reviewer = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user_reviews'
        )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='reviews'
        )
    title = models.CharField(max_length=80, blank=False)
    content = models.CharField(max_length=500, blank=False)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True, null=True)
    approved = models.BooleanField(default=False)
    rating = models.IntegerField(null=True, blank=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.service.calculate_average_rating()

    def delete(self, *args, **kwargs):
        service = self.service
        super().delete(*args, **kwargs)
        service.calculate_average_rating()

    def __str__(self):
        return self.title
