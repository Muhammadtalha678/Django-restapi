from rest_framework import serializers
from .models import Book,Category,Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id','title'
        )
        model = Category

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'category_id',
            'isbn',
            'pages',
            'price',
            'stock',
            'description',
            'imageUrl',
            'status',
            'date_created'
            )
        model = Book


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'product_tag',
            'name',
            'category_id',
            'price',
            'stock',
            'imageUrl',
            'status',
            'date_created',
            )
        model = Product
