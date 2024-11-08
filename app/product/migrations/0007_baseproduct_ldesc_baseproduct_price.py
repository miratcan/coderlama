# Generated by Django 5.1.3 on 2024-11-08 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0006_rename_image_baseproduct_image_1"),
    ]

    operations = [
        migrations.AddField(
            model_name="baseproduct",
            name="ldesc",
            field=models.TextField(
                blank=True, help_text="Markdown formatted text", null=True
            ),
        ),
        migrations.AddField(
            model_name="baseproduct",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
