import os
from firebase_admin import messaging
from firebase_admin import credentials
import firebase_admin
from bs4 import BeautifulSoup
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django

django.setup()
from users.models import User

cred = credentials.Certificate("fir-test-d20b3-firebase-adminsdk-u3j7c-f95f9b1e7d.json")
firebase_admin.initialize_app(cred)


def send_to_androidapp(token):
    registration_token = token

    message = messaging.Message(
        android=messaging.AndroidConfig(
            notification=messaging.AndroidNotification(
                title="변경!",
                body="변화가 감지됬어요!",
                default_sound=True,
                visibility="public",
                priority="high",
            )
        ),
        token=registration_token,
    )
    response = messaging.send(message)
    print("Successfully sent message:", response)


if __name__ == "__main__":
    try:
        print("test")
        user_obj = User.objects.get(pk=6)
        send_to_androidapp(user_obj.token)
    except:
        print("error")
