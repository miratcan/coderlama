# Generated by Django 5.1.3 on 2024-11-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0007_baseproduct_ldesc_baseproduct_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="baseproduct",
            name="link",
            field=models.URLField(null=True),
        ),
    ]
