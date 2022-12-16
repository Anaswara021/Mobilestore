from django.shortcuts import render,redirect
# from django.http import HttpResponse
from django.views.generic import View
from django.contrib import messages
from .form import RegistrForm
from .models import Registration

# Create your views here.
 


def ho(request):
    return render(request,"home.html")

def lo(request):
    return render(request,"logsr.html")


def mho(request):
    return render(request,"mhome.html")


class Registr(View):
    def get(self,request):
        form =RegistrForm()
        return render(request,"Registr.html",{"form":form})
    def post(self,req):
        form_data=RegistrForm(req.POST)
        if form_data.is_valid():
            print(form_data.cleaned_data)
            uid=form_data.cleaned_data.get('uid')
            name=form_data.cleaned_data.get('name')
            phno=form_data.cleaned_data.get('phone')
            em=form_data.cleaned_data.get('email')
            Registration.objects.create(uid=uid,name=name,phno=phno,email=em)
            messages.success(req,"Registration completed successfully")
            return redirect('Registr')
        else:
            messages.error(req,"Registraton faild")
            return render(req,"Registr.html",{"form":form_data})
