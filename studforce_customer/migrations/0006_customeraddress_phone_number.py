# Generated by Django 5.1.1 on 2024-10-08 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("studforce_customer", "0005_cart_size_cart_type_size"),
    ]

    operations = [
        migrations.AddField(
            model_name="customeraddress",
            name="phone_number",
            field=models.CharField(
                default="", max_length=15, verbose_name="Phone Number"
            ),
        ),
    ]
