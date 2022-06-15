# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer
from .models import Category

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    """Serialize data to JSON format.
    By firing a query set.
    and using a serializer class.
    """

    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
