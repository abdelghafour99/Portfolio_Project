from django.contrib import admin
from .models import product, category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id_cat' ,'image']

class ProductAdmin(admin.ModelAdmin):
    list_filter = ['title', 'category', 'price', 'create', 'available', 'nbr_achat', 'nbr_recemmend']



admin.site.register(category, CategoryAdmin)
admin.site.register(product, ProductAdmin)