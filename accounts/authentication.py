import requests
from django.contrib.auth import get_user_model
User = get_user_model()

PERSONA_VERIFY_URL = 'https://verifier.login.persona.org/verify'
DOMAIN = 'localhost'

class PersonaAuthenticationBackend(object):

    def authenticate(self, assertion):
        print('ok here')
        response = requests.post(
            PERSONA_VERIFY_URL,
            data = {'assertion': assertion, 'audience': DOMAIN}
        )
        print(response)
        if response.ok and response.json()['status'] == 'okay':
            print('response ok')
            email = response.json()['email']
            print(email)
            try:
                user = User.objects.get(email = email)
                print user
                return user
            except User.DoesNotExist:
                user = User.objects.create(email = email)
                print('not exist', user)
                return user

    def get_user(self, email):
        try:
            return User.objects.get(email = email)
        except User.DoesNotExist:
            return None