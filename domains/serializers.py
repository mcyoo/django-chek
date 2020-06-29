from rest_framework import serializers
from .models import Domain


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("title", "url", "change")
        model = Domain
