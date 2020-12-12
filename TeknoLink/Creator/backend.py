from django.contrib.auth.backends import BaseBackend
from .models import User

class MyBackend(BaseBackend):
    def authenticate(self, request, user_id=None, password=None):
        user=User.objects.get(user_id=user_id)
        if user is not None:
            if password == user.password:
                return user
        return None
    def get_user(self,user_id):
        try:
            return User.objects.get(user_id=user_id)
        except User.DoesNotExist:
            return None