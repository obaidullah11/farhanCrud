from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=255)
    category_arabic = models.CharField(max_length=255)

    def __str__(self):
        return self.category

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='subcategories/images/')
    name = models.CharField(max_length=255)
    name_arabic = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_arabic = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    description_arabic = models.TextField(blank=True)

    def __str__(self):
        return self.name
