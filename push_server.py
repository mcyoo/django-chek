from firebase_admin import messaging
from firebase_admin import credentials
import firebase_admin
from firebase_admin import auth

cred = credentials.Certificate("fir-test-d20b3-firebase-adminsdk-u3j7c-f95f9b1e7d.json")
firebase_admin.initialize_app(cred)

# This registration token comes from the client FCM SDKs.
registration_token = "foc1bYvVmj4:APA91bGuO5gx1y1uSUSmtlbo3nB78dv3s0yldalB868-37qAiMQ4g9NndgmaTAyG8xl9iyVlrHTdPksnwPSR5qRt1Qy2AHxK5T_3JN4lXjghlULKkahbg2_V9tcvzUtHKqSr82_QD0wJ"

# See documentation on defining a message payload.
message = messaging.Message(
    android=messaging.AndroidConfig(
        notification=messaging.AndroidNotification(
            title="변경!",
            body="변화가 감지됬어요!",
            default_sound=True,
            # visibility="public",
            priority="high",
        )
    ),
    # notification=messaging.Notification(title="변경!", body="변화가 감지됬어요!",),
    token=registration_token,
)

# Send a message to the device corresponding to the provided
# registration token.
response = messaging.send(message)
# Response is a message ID string.
print("Successfully sent message:", response)

