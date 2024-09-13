from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Subcategory
from .serializers import *

@api_view(['POST'])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_subcategory(request):
    serializer = SubcategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def get_all_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    
    # Format the data as needed
    formatted_data = [
        {
            "category": item['category'],
            "categoryArabic": item['category_arabic']
        }
        for item in serializer.data
    ]
    
    response = {
        "success": True,
        "message": "Data fetched successfully",
        "data": formatted_data
    }
    
    return Response(response)


@api_view(['GET'])
def get_categories_with_subcategories(request):
    categories = Category.objects.all()
    serializer = CategoryWithSubcategoriesSerializer(categories, many=True)
    
    # Format data as requested
    formatted_data = [
        {
            "category": item['category'],
            "categoryArabic": item['category_arabic'],
            "subcategories": [
                {
                    "image": subcategory['image'],
                    "name": subcategory['name'],
                    "nameArabic": subcategory['name_arabic'],
                    "price": subcategory['price'],
                    "priceArabic": subcategory['price_arabic'],
                    "description": subcategory['description'],
                    "descriptionArabic": subcategory['description_arabic']
                } for subcategory in item['subcategories']
            ]
        }
        for item in serializer.data
    ]
    
    response = {
        "success": True,
        "message": "Data fetched successfully",
        "data": formatted_data
    }
    
    return Response(response)
@api_view(['PUT', 'PATCH'])
def update_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return Response({"success": False, "message": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CategoryUpdateSerializer(category, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response({
            "success": True,
            "message": "Category updated successfully",
            "category": serializer.data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            "success": False,
            "message": "Invalid data",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT', 'PATCH'])
def update_subcategory(request, subcategory_id):
    try:
        subcategory = Subcategory.objects.get(id=subcategory_id)
    except Subcategory.DoesNotExist:
        return Response({"success": False, "message": "Subcategory not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = SubcategoryUpdateSerializer(subcategory, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response({
            "success": True,
            "message": "Subcategory updated successfully",
            "subcategory": serializer.data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            "success": False,
            "message": "Invalid data",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return Response({"success": False, "message": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

    category.delete()
    return Response({
        "success": True,
        "message": "Category deleted successfully"
    }, status=status.HTTP_200_OK)
@api_view(['DELETE'])
def delete_subcategory(request, subcategory_id):
    try:
        subcategory = Subcategory.objects.get(id=subcategory_id)
    except Subcategory.DoesNotExist:
        return Response({"success": False, "message": "Subcategory not found"}, status=status.HTTP_404_NOT_FOUND)

    subcategory.delete()
    return Response({
        "success": True,
        "message": "Subcategory deleted successfully"
    }, status=status.HTTP_200_OK)
