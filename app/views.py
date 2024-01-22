from django.shortcuts import render

# Create your views here.

from app.forms import *
from django.http import HttpResponse

from django.core.mail import send_mail

def registeration(request):
    ufo=Userform()
    pfo=Profileform()
    d={'ufo':ufo,'pfo':pfo}
    if request.method=='POST' and request.FILES:
        ufd=Userform(request.POST)
        pfd=Profileform(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            MUFDO=ufd.save(commit=False)
            pw=ufd.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()

            MPFDO=pfd.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            send_mail('Registeration Process',
                      'Thank You Registration is Successfull!!!',
                      'vamsifun4@gmail.com',
                      [MUFDO.email],
                      fail_silently=False)


            return HttpResponse('Registration Succesfull')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'registeration.html',d)

# twcl hnpe fnxn hhgj













        







