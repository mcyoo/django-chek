from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import DomainSerializer
from .models import Domain
from users.models import User
import jwt
from django.conf import settings


class DomainView(APIView):
    def post(self, request):
        print(request.data)
        try:
            header = request.META.get("HTTP_AUTHORIZATION")
            if header is not None:
                token = header
                decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                pk = decoded.get("pk")
                user = User.objects.get(pk=pk)

                serializer = DomainSerializer(
                    data=request.data, context={"token": user}
                )
                if serializer.is_valid():
                    domain = serializer.save()
                    return Response(status=status.HTTP_200_OK)
                # return Response(DomainSerializer(user.domains.all(), many=True).data)
        except (ValueError, User.DoesNotExist, Domain.DoesNotExist, IndexError):
            pass
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        print(request.data)
        try:
            index = request.data.get("index")
            print(index)
            header = request.META.get("HTTP_AUTHORIZATION")
            if header is not None:
                token = header
                decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                pk = decoded.get("pk")
                user = User.objects.get(pk=pk)
                domain = user.domains.all()[index]
                print(domain)
                domain.delete()
                return Response(status=status.HTTP_200_OK)
                # return Response(DomainSerializer(user.domains.all(), many=True).data)
        except (ValueError, User.DoesNotExist, Domain.DoesNotExist, IndexError):
            pass
        return Response(status=status.HTTP_400_BAD_REQUEST)


"""
@api_view(["GET", "POST"])
def save_token(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        token = json_data["firebase_token"]
        user_os = json_data["user_os"]
        user_ver = json_data["user_ver"]
        print(token)
        try:
            user = models.User.objects.get(token=token)
            if user.domains.count() > 0:
                data = serializers.serialize(
                    "json", user.domains.all(), fields=("url", "title", "change")
                )
                response = HttpResponse(content=data)
                return response
        except models.User.DoesNotExist:
            models.User.objects.create(token=token, user_os=user_os, user_ver=user_ver)
    return Response(status=status.HTTP_200_OK)
"""

