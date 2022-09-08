from django.contrib import admin

# Register your models here.
from .models import Book,Category,Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Product)