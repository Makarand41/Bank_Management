# Generated by Django 4.2.7 on 2024-01-30 14:08

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AllUsers01",
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
                ("email", models.EmailField(max_length=254)),
                ("dob", models.DateField()),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
