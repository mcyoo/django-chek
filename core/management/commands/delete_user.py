from django.core.management.base import BaseCommand
from users.models import User
from domains.models import Domain


def delete_user(token):
    try:
        user = User.objects.get(token=token)
        print("delete_user : token is invaild i will delete:", user)
        user.delete()
    except:
        pass


class Command(BaseCommand):

    help = "delete token"

    def handle(self, *args, **options):
        # delete_user('')
        print("asdf")
        self.stdout.write(self.style.SUCCESS(f"Everything success"))
