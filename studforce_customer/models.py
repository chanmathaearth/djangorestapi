from django.db import models
from studforce_auth.models import Customer
from studforce_product.models import Product, Promotion

class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Customer")
    street_address = models.CharField(max_length=100, verbose_name="Street Address")
    province = models.CharField(max_length=100, verbose_name="Province")
    district = models.CharField(max_length=100, verbose_name="District")
    subdistrict = models.CharField(max_length=100, verbose_name="Subdistrict")
    postal_code = models.CharField(max_length=10, verbose_name="Postal Code")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number", default="")    
    
    def __str__(self):
        return f"{self.street_address}, {self.subdistrict}, {self.district}, {self.province}, {self.postal_code}"

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
    type_size = models.CharField(max_length=10, default='EUR')
    size = models.CharField(max_length=10, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.customer.username} with {self.product.name}"
