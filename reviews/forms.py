from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    """
    A form for creating a service review. The user must enter a title
    for the review, the review content, and a rating between 1 and 5.
    The user is automatically linked to the review as the review owner
    and the date the review is created/edited is updated on saving.
    """

    class Meta:
        """
        Meta class for the form's metadata. Specifies the model to use
        and which fields to display to the user.
        """

        model = Review
        fields = {
            'title',
            'rating',
            'content',
        }
        labels = {
            'title': '',
            'rating': '',
            'content': '',
        }
        widgets = {
            'title': forms.TextInput(
                attrs = {
                    'placeholder': 'Title *'
                }
            ),
            'content': forms.Textarea(
                attrs = {
                    'placeholder': 'Write a review... *',
                    'style': 'height: 200px;',
                }
            ),
            'rating': forms.RadioSelect(
                choices = [
                    (1,'★'), (2,'★'), (3,'★'), (4,'★'), (5,'★'),
                ],
                attrs = {
                    'class': 'review-stars'
                }
            ),
        }
    
    field_order = [
        'title',
        'content',
        'rating',
    ]