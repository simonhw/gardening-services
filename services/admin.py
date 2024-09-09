from django.contrib import admin
from .models import Category
from .models import Service
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Service)
class ServiceAdmin(SummernoteModelAdmin):

    summernote_fields = {'description'}

admin.site.register(Category)