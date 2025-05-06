# test_project/members/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name',  'display_image','price', 'description']  # Add display_image
    list_editable = ['price', 'description']
    list_filter = ['price']
    search_fields = ['name', 'description']

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "No Image"
    display_image.short_description = 'Image'