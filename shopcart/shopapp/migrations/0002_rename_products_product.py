# Generated by Django 4.1.5 on 2023-02-02 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shopapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Products",
            new_name="Product",
        ),
    ]
