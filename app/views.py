from django.shortcuts import render

# Create your views here.

from app.forms import *

def registeration(request):
    ufo=Userform()
    pfo=Profileform()
    d={'ufo':ufo,'pfo':pfo}
    return render(request,'registeration.html',d)