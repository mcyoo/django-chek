from rest_framework import generics
from .serializers import DomainSerializer
from .models import Domain


class ListUser(generics.ListCreateAPIView):

    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
