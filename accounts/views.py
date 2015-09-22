from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def persona_login(request):
    print('authenticating')
    user = authenticate(assertion = request.POST['assertion'])
    print('userrrr')
    if user:
        login(request, user)
    return HttpResponse('OK')