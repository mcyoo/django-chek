from firebase_admin import messaging
from firebase_admin import credentials
import firebase_admin
from firebase_admin import auth

cred = credentials.Certificate("fir-test-d20b3-firebase-adminsdk-u3j7c-f95f9b1e7d.json")
firebase_admin.initialize_app(cred)

# This registration token comes from the client FCM SDKs.
registration_token = "fnW2sId-8fI:APA91bHn8ol60dqGk1KkZYQXLj39FZVGZ_2nNKMFCzVEWVfLybQC13MXUX0N7hGyKz_RdWmx7CA9nzQVSfD_K89ytP4ZDV-cYl91oLq8GjUXa494A1kz59iKae1aqq3EA9iL-l5_duAQ"

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

