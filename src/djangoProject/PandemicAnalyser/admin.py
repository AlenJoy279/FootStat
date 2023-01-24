from django.contrib import admin

# Register your models here.
from .models import * # Add this import

admin.site.register(Tweet)
# admin.site.register(<Another Model>)
