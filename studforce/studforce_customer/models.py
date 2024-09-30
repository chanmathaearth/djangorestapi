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
        UK = "UK"
        CM = "CM"

    type_size = models.CharField(max_length=10, choices=TypeSize.choices, default=TypeSize.EUR)
    size = models.CharField(max_length=10)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='size')

class Customer(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    birthdate = models.DateField(null=False)
    email = models.EmailField(max_length=254, unique=True, null=False)
    phone = models.CharField(max_length=20, null=False)
    username = models.CharField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=100, null=False)
    gender = models.CharField(max_length=20, null=False, choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))
    def __str__(self):
        return self.username


class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Customer")
    street_address = models.CharField(max_length=100, verbose_name="Street Address")
    province = models.CharField(max_length=100, verbose_name="Province")
    district = models.CharField(max_length=100, verbose_name="District")
    subdistrict = models.CharField(max_length=100, verbose_name="Subdistrict")
    postal_code = models.CharField(max_length=10, verbose_name="Postal Code")

    def __str__(self):
        return f"{self.street_address}, {self.subdistrict}, {self.district}, {self.province}, {self.postal_code}"


class Promotion(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.code


class Order(models.Model):
    promotion = models.ForeignKey(Promotion, on_delete=models.SET_NULL, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='ProductOrder')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Pending')
    payment_status = models.CharField(max_length=20, choices=[('Paid', 'Paid'), ('Pending', 'Pending')], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer.username}"


class ProductOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Product {self.product.name} in Order {self.order.id}"


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.customer.username} with {self.product.name}"


class Administrator(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
