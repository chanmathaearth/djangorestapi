from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    brand = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    image = models.CharField(max_length=255)
    amount = models.PositiveIntegerField(default=0)
    categories = models.ManyToManyField(ProductCategory)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    image = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

class ProductSize(models.Model):
    class TypeSize(models.TextChoices):
        EUR = "EUR"
        US = "US"

    type_size = models.CharField(max_length=10, choices=TypeSize.choices, default=TypeSize.EUR)
    size = models.CharField(max_length=10)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='size')

class Promotion(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.code
