from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *

urlpatterns = [
    # Category URLs
    path('create-category/', create_category, name='create-category'),
    path('create-subcategory/',create_subcategory, name='create-subcategory'),
    path('getallcategories/', get_all_categories, name='get-all-categories'),
    path('getallsubcategory/', get_categories_with_subcategories, name='get-categories-with-subcategories'),
    path('category-update/<int:category_id>/', update_category, name='update-category'),
    path('subcategory-update/<int:subcategory_id>/', update_subcategory, name='update-subcategory'),
    path('category-delete/<int:category_id>/', delete_category, name='delete-category'),
    path('subcategory-delete/<int:subcategory_id>/',delete_subcategory, name='delete-subcategory'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
