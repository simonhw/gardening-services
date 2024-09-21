from django.db import models
from accounts.models import CustomUser
from services.models import Service

class Review(models.Model):
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
    title = models.TextField(max_length=80, blank=False)
    content = models.TextField(max_length=500, blank=False)
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