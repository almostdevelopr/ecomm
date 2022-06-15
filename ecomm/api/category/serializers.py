from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.Serializer):
    """Serialize the category model."""

    class Meta:
        model = Category
        field = ("name", "description")
