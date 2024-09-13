from django.contrib import admin
from .models import Category, Subcategory

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'category_arabic']
    search_fields = ['category', 'category_arabic']

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'image']
    search_fields = ['name', 'category__category']
    list_filter = ['category']
