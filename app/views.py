from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail

def registration(request):
    UFEO = UserForm()
    PFEO = ProfileForm()
    d = {'UFEO':UFEO,'PFEO':PFEO}
    if request.method == 'POST' and request.FILES:
        UFDO = UserForm(request.POST)
        PFDO = ProfileForm(request.POST,request.FILES)
        if UFDO.is_valid() and PFDO.is_valid():
            MUFDO = UFDO.save(commit=False)
            MUFDO.set_password(UFDO.cleaned_data['password'])
            MUFDO.save()
            MPFDO = PFDO.save(commit=False)
            MPFDO.username = MUFDO
            MPFDO.save()

            send_mail(
                'registration',
                'registration successfull',
                'neeteshsingh9575@gmail.com',
                [MUFDO.email],
                fail_silently=False
            )

            return HttpResponse('registration successful')

    return render(request,'registration.html',d)


def home(request):
    return render(request,'home.html')