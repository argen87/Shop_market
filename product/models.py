from fileinput import filename

from ckeditor.fields import RichTextField
from django.db import models
import os
import random


def upload_image_path(instance, filename):
    print(instance, filename)
    new_name = random.randint(1000000, 9999999)
    name, ext = Product.get_filename_ext(filename)
    final_name = f'{new_name}{ext}'
    return f'products/images/{new_name}/{final_name}'


class DataABC(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(DataABC):
    slug = models.SlugField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = RichTextField()
    quantity = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=False)
    preview = models.ImageField(upload_to=upload_image_path)

    @staticmethod
    def get_filename_ext(filepath):
        # helloworldmynameis.jpg
        base_name = os.path.basename(filepath)
        name, ext = os.path.splitext(base_name)
        return name, ext















