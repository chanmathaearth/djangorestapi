from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    birthdate = models.DateField(null=False)
    email = models.EmailField(max_length=254, unique=True, null=False)
    gender = models.CharField(max_length=20, null=False, choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))
    groups = models.ManyToManyField('auth.Group', related_name='customer_user_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customer_permission_set', blank=True)

    def __str__(self):
        return self.username


class Administrator(AbstractUser):
    groups = models.ManyToManyField('auth.Group', related_name='administrator_user_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='administrator_permission_set', blank=True)

    def __str__(self):
        return self.username
