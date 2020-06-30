from django.shortcuts import render, HttpResponse, redirect, reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
import json
from django.core import serializers


@csrf_exempt
def save_token(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        token = json_data["firebase_token"]
        user_os = json_data["user_os"]
        user_ver = json_data["user_ver"]
        print(token)
        try:
            user = models.User.objects.get(token=token)
            # domain_dict = {}
            # i = 0
            if user.domains.count() > 0:
                data = serializers.serialize(
                    "json", user.domains.all(), fields=("url", "title", "change")
                )
                response = HttpResponse(content=data)
                return response

                # return redirect("domains:data_obj")
                """
                for domain_data in user.domains.all():
                    domain_dict.update(
                        {
                            i: {
                                "title": domain_data.title,
                                "url": domain_data.url,
                                "change": domain_data.change,
                            }
                        }
                    )
                    i += 1
                    
                print(domain_dict)
            return JsonResponse(domain_dict, json_dumps_params={"ensure_ascii": True})
            """

        except models.User.DoesNotExist:
            models.User.objects.create(token=token, user_os=user_os, user_ver=user_ver)
    return HttpResponse("")
