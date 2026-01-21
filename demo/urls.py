from django.urls import path
from . import views

app_name = "demo"

urlpatterns = [
    path("demo/", views.demo_list, name="demo_list"),
]
