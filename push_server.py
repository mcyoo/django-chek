from firebase_admin import messaging
from firebase_admin import credentials
import firebase_admin
from firebase_admin import auth

cred = credentials.Certificate("fir-test-d20b3-firebase-adminsdk-u3j7c-f95f9b1e7d.json")
firebase_admin.initialize_app(cred)

# This registration token comes from the client FCM SDKs.
registration_token = "e9pZKHuwtEoYqMLNdisG1u:APA91bFxumfW8r9lZ98L5Y4nTJzLm12uv8dWHkbGsRSwP1tkoZTvPzCOufvNvocoFV63AvTjmz226ipoi0O4UriDRBKQ-zFp7eUeWcdz76VSWzLFhFE4efBt6yIJUUaozRIhMtGWnhGl"

# See documentation on defining a message payload.
"""
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
"""
message = messaging.Message(
    notification=messaging.Notification(title="test", body="페이지 변경 감지!"),
    apns=messaging.APNSConfig(
        payload=messaging.APNSPayload(
            aps=messaging.Aps(
                alert=messaging.ApsAlert(title="test", body="페이지 변경 감지!",), badge=42,
            ),
        ),
    ),
    token=registration_token,
)

# Send a message to the device corresponding to the provided
# registration token.
response = messaging.send(message)
# Response is a message ID string.
print("Successfully sent message:", response)

