from django.urls import path
from . import views

app_name = "setup"

urlpatterns = [
    path("setup/", views.setup, name="setup"),
]
