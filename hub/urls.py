from django.urls import path
from . import views

app_name = "hub"

urlpatterns = [
    path("hub/", views.hub_list, name="hub_list"),
]
