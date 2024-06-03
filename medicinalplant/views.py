from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
# FILE UPLOAD AND VIEW
from  django.core.files.storage import FileSystemStorage
# SESSION
from django.conf import settings
from .models import *
import os
from ML import test
from keras import backend as K

def first(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')

def addregister(request):
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('address')
        c=request.POST.get('phone')
        d=request.POST.get('email')
        e=request.POST.get('password')
        f=regtable(name=a,address=b,phone=c,email=d,password=e)
        f.save()

    return render(request,'register.html')

def addlogin(request):
    email=request.POST.get('email')
    password=request.POST.get('password')

    if email=="admin@gmail.com" and password=="admin":
        request.session['detail']=email
        request.session['admin']='admin'
        return render(request,'index.html')

    elif regtable.objects.filter(email=email,password=password).exists():
     user=regtable.objects.get(email=email,password=password)
     request.session['uid']=user.id
     return render(request,'index.html')

    else:
        return render(request,'login.html')

def fileupload(request):
    '''if request.method=="POST":
        a=request.POST.get('name')
        b=request.FILES['image']
        fs=FileSystemStorage()
        file=fs.save(b.name,b)
        ins=fileuploadtable(name=a,image=file)
        ins.save()        
    return render(request,'fileupload.html')'''
    
    if request.method=="POST":
        u_id = request.session['uid']
        
        file = request.FILES['image']
        try:
            os.remove("media/input/test/test.jpg")
        except:
            pass
        
        
        fs = FileSystemStorage(location="media/input/test")
        fs.save("test.jpg",file)
        K.clear_session()
        result=test.predict()
 
        cus=fileuploadtable(image=file)
        cus.save()
       
        return render(request,'result.html',{'result':result})
    else:
        return render(request,'fileupload.html')



def logout(request):
    session_keys=list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(index)

def v_register(request):
    h=regtable.objects.all()
    return render(request,'v_register.html',{'result':h})
