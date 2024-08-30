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
