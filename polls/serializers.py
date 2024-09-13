from rest_framework import serializers
from .models import Category, Subcategory
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category', 'category_arabic']

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'category', 'image', 'name', 'name_arabic', 'price', 'price_arabic', 'description', 'description_arabic']




class CategoryWithSubcategoriesSerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['category', 'category_arabic', 'subcategories']

    def get_subcategories(self, obj):
        subcategories = Subcategory.objects.filter(category=obj)
        return SubcategorySerializer(subcategories, many=True).data
    


class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category', 'category_arabic']

# Serializer for updating Subcategory
class SubcategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['category', 'image', 'name', 'name_arabic', 'price', 'price_arabic', 'description', 'description_arabic']