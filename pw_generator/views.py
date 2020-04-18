from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):

    # context = {'pw':'221qpaz554a'}

    return render(request,'pw_generator/home.html')


def about(request):

    greet = 'thankyou for visit!'

    return render(request,'pw_generator/about.html',{'greeting':greet})

def password(request):

    chars = list('qwertyuiopasdfghjklzxcvbnm')

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):

        chars.extend([i.upper() for i in chars])

    if request.GET.get('specialchars'):

        chars.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):

         chars.extend(str([x for x in range(10)]))

    pw = ''

    for x in range(length):

        pw += random.choice(chars)

    return render(request,'pw_generator/password.html',{'password':pw})