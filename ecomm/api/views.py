# from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):
    """A home page."""
    return JsonResponse({"info": "Django E-Com Project", "name": "Ecomm"})
