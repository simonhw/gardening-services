from django.db import models
from accounts.models import UserAccount
from services.models import Service

class Review(models.Model):
    reviewer = models.ForeignKey(
        UserAccount,
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
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    rating = models.IntegerField

    def __str__(self):
        return self.title