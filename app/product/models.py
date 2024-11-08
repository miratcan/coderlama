from django.db import models
from django.db.models import (
    CharField, SlugField, DateTimeField, TextField,
    ImageField, ManyToManyField, Model, URLField
)
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.urls import reverse


class Tag(Model):
    name = CharField(max_length=100)
    slug = SlugField(max_length=100)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    STATUS_CHOICES = [
        ('published', 'Published'),
        ('draft', 'Draft'),
        ('deleted', 'Deleted')
    ]
    status = CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )

    def __str__(self):
        return self.name


class BaseProduct(Model):
    name = CharField(max_length=200)
    upc = CharField(unique=True, max_length=12, null=True, blank=True)
    sdesc = CharField(
        verbose_name="Short Description",
        max_length=255,
        validators=[
            MinLengthValidator(200),
            MaxLengthValidator(255)
        ],
        null=True,
    )
    ldesc = TextField(
        verbose_name="Long Description",
        null=True,
        blank=True,
        help_text="Markdown formatted text"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    image_1 = ImageField(upload_to='product_images', null=True)
    image_2 = ImageField(upload_to='product_images', null=True, blank=True)
    image_3 = ImageField(upload_to='product_images', null=True, blank=True)
    link = URLField(null=True, blank=False)
    tags = ManyToManyField(Tag, blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])

class AmazonProduct(BaseProduct):
    asin = CharField(max_length=10)
