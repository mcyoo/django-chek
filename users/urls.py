from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("token/", views.save_token, name="save-token"),
]
