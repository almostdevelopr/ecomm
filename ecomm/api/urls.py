from django.urls import path, include
from .views import home

# from rest_framework.authtoken import views
app_name = "api"
urlpatterns = [
    path("", home, name="api.home"),
    # path("category/", include("api.category.urls")),
]
