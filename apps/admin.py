from django.contrib import admin
from .models import Instagram

@admin.register(Instagram)
class Instagram(admin.ModelAdmin):
    list_display = ("username","password")
