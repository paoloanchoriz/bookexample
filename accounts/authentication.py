import requests
import sys
from django.contrib.auth import get_user_model
User = get_user_model()

PERSONA_VERIFY_URL = 'https://verifier.login.persona.org/verify'
DOMAIN = 'localhost'

class PersonaAuthenticationBackend(object):

    def authenticate(self, assertion):
        response = requests.post(
            PERSONA_VERIFY_URL,
            data = {'assertion': assertion, 'audience': DOMAIN}
        )
        if response.ok and response.json()['status'] == 'okay':
            email = response.json()['email']
            try:
                user = User.objects.get(email = email)
                return user
            except User.DoesNotExist:
                user = User.objects.create(email = email)
                return user

    def get_user(self, email):
        try:
            return User.objects.get(email = email)
        except User.DoesNotExist:
            return None