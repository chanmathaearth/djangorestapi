# Generated by Django 5.1.1 on 2024-10-08 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "studforce_auth",
            "0002_alter_administrator_options_alter_customer_options_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="phone",
        ),
    ]
