from rest_framework import serializers
from .models import Domain


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("title", "url", "change")
        model = Domain
        read_only_fields = ("title", "change")

    def create(self, validated_data):
        token = self.context.get("token")
        domain = Domain.objects.create(**validated_data, token=token)
        return domain
