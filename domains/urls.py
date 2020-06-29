from django.urls import path
from . import views

app_name = "domains"

urlpatterns = [
    # path("register/", views.register_domain, name="register-domain"),
    path("data/", views.ListUser.as_view(), name="data_obj"),
]
