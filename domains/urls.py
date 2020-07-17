from django.urls import path
from . import views

app_name = "domains"

urlpatterns = [
    # path("register/", views.register_domain, name="register-domain"),
    path("del/", views.DomainView.as_view(), name="delete"),
]
