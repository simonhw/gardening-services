from django.contrib import admin
from .models import Review
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):

    model = Review
    list_display = (
        'pk', 'title', 'service', 'rating', 'reviewer',
        'created_on', 'updated_on', 'approved'
        )

    summernote_fields = {'content'}

    ordering = ('created_on',)
