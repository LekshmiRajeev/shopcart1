# Generated by Django 4.1.5 on 2023-02-04 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shopapp", "0002_rename_products_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("locality", models.CharField(max_length=200)),
                ("city", models.CharField(max_length=50)),
                ("mobile", models.IntegerField(default=0)),
                ("zip", models.IntegerField()),
                (
                    "state",
                    models.CharField(
                        choices=[
                            (
                                "Andaman and Nicobar Island",
                                "Andaman and Nicobar Island",
                            ),
                            ("Andra pradesh", "Andra pradesh"),
                            ("Assam", "Assam"),
                            ("Bihar", "Bihar"),
                            ("Kerala", "Kerala"),
                            ("Delhi", "Delhi"),
                            ("Goa", "Goa"),
                            ("Hariyana", "Hariyana"),
                            ("Punjab", "Punjab"),
                            ("Rajasthan", "Rajasthan"),
                            ("Tamilnadu", "Tamilnadu"),
                            ("Karnataka", "Karnataka"),
                            ("WestBengal", "WestBengal"),
                            ("Uttarpradesh", "Uttarpradesh"),
                            ("Madhyapradesh", "Madhyapradesh"),
                            ("Gujarat", "Gujarat"),
                            ("Meghalaya", "Meghalaya"),
                            ("Mizoram", "Mizoram"),
                            ("Odisa", "Odisa"),
                            ("Nagaland", "Nagaland"),
                            ("Sikkim", "Sikkim"),
                            ("Uttarakhand", "Uttarakhand"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
