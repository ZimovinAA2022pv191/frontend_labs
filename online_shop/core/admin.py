from django.contrib import admin

from core.models import Product


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['__all__']