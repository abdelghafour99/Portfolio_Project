from django.conf import Settings
from django.db import models
# Create your models here.
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime


class category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Category")
    id_cat = models.IntegerField(verbose_name="Id_Category")
    image = models.ImageField(verbose_name="Image_Category")

    def __str__(self):
        return self.name

    class Meta:
        ordering=['name']
        verbose_name_plural='category'

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'pk': self.id})

class product(models.Model):
    title = models.CharField(max_length=150, verbose_name="Product")
    category = models.ForeignKey(category, related_name='products', verbose_name='Product_Category', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Image")
    discription = models.TextField(blank=True, null=True, verbose_name="Description")
    qte = models.CharField(max_length=50, verbose_name="Quantity")
    price = models.DecimalField(decimal_places=2, max_digits=100000, verbose_name="Price")
    nbr_achat = models.BinaryField(verbose_name="Number_buy")
    available = models.BooleanField(default=True, verbose_name="Still_available")
    create = models.TimeField(auto_now_add=True, verbose_name="Date")
    nbr_recemmend = models.IntegerField(default=0, verbose_name="Likes")
    percent_discount = models.IntegerField(default=0, verbose_name="Percent_DCR")

    def priceTax(self):
        return int(self.price - ((self.price * self.percent_discount)/100))

    class Meta:
        ordering = ['create']
        verbose_name_plural = 'product'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.id})
