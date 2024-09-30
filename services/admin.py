from django.contrib import admin
from .models import Category
from .models import Service
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Service)
class ServiceAdmin(SummernoteModelAdmin):

    model = Service
    list_display = (
        'name', 'average_rating', 'review_count',
        )

    summernote_fields = {'description'}


admin.site.register(Category)
