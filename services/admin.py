from django.contrib import admin
from .models import Category
from .models import Service

admin.site.register(Category)
admin.site.register(Service)