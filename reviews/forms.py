from .models import Review
from django import forms
from django.core.exceptions import ValidationError


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
                attrs={
                    'placeholder': 'Title *'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'placeholder': 'Write a review... *',
                    'style': 'height: 200px;',
                }
            ),
            'rating': forms.RadioSelect(
                choices=[
                    (1, '★'), (2, '★'), (3, '★'), (4, '★'), (5, '★'),
                ],
            ),
        }

    field_order = [
        'title',
        'content',
        'rating',
    ]

    def clean(self):
        """
        Validation of form data on the back end.

        The method ensures that input fields cannot be blank.

        If the data validates, the method returns the cleaned data.
        If invalid, it raises a validation error to inform the user.
        """

        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        rating = cleaned_data.get('rating')

        if not title:
            raise ValidationError('You must provide a title.')

        if not content:
            raise ValidationError('You must write a review.')

        if not rating:
            raise ValidationError('You must provide a rating.')

        return cleaned_data
