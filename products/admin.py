from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)