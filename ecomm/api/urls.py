import imp
from django.urls import path, include
from .views import home

# from rest_framework.authtoken import views

urlpatterns = [path("", home, name="api.home")]
