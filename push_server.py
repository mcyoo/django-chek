from firebase_admin import messaging
from firebase_admin import credentials
import firebase_admin

cred = credentials.Certificate("fir-test-d20b3-firebase-adminsdk-u3j7c-f95f9b1e7d.json")
firebase_admin.initialize_app(cred)

# This registration token comes from the client FCM SDKs.
registration_token = "eakZIZkx6Zg:APA91bEXEQKySn45bG3vUm6B3klQpi4oKkwoQf1j_YcWS31orZK7kZEMq5q0RK0wwrr68Y8HPT29HpfQtcWng634SUKpBkUMBorvaZWXcTKfnY2Y5VyBb8g96yZUmHf837dmttSqbhuG"

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

