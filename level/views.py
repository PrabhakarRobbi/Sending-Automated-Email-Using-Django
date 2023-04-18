# from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.models import  User
from django.contrib import messages
from django.conf import settings
from . models import FormData
from .form import Registration

# Create your views here.
def Home(request):
    return render(request,'level/Home.html')

def Page(request):    
    return render(request,'level/Page.html')

def success(request):
    return render(request,'level/success.html')

def message(request):
    return render(request,'level/message.html')

# This is for save the form data in the backend, send automated mail and validation if the email is exist or not 
def register(request):
    if request.method =='POST':
        email = request.POST['email']
        username = request.POST['username']
        fm = Registration(request.POST)

        if User.objects.filter(username=username).exists():
             messages.info(request, 'Username already exist')
             return redirect("level:register")
        
        # elif User.objects.filter(email=email).exists():
        #      messages.info(request, 'Email was already Taken !')
        #      return redirect("level:register")

        elif fm.is_valid():
            nm=fm.cleaned_data['username']
            em=fm.cleaned_data['email']
            pm=fm.cleaned_data['phone']
            reg=FormData(username=nm,email=em,phone=pm)
            reg.save()
            fm = Registration()

        user = User.objects.create_user(username=username, email=email)
        mydict = {'username': username}
        user.save()
        html_template = 'level/message.html'
        html_message = render_to_string(html_template, context=mydict)
        subject = 'Welcome to Levelup'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        message = EmailMessage(subject, html_message,email_from, recipient_list)
        message.content_subtype = 'html'
        message.send()
        return redirect("level:success")
    
    else:
        fm = Registration()
    return render(request,'level/register.html')

# This for display the backend data in the front end
def Display(request):
    stud=FormData.objects.all()
    return render(request,'level/Display.html',{'stu':stud})

#This is for delete the data from front end
def delete_data(request,id):
    if request.method=='POST':
        pi = FormData.objects.get(pk=id)
        pi.delete()
        messages.info(request, 'User Info is Deleted')
        return redirect("level:Display")

#This for Update the data
def Update(request,id):
    if request.method=='POST':
        pi=FormData.objects.get(pk=id)
        fm=Registration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.info(request, 'User Info is Updated')

    else:
        pi=FormData.objects.get(pk=id)
        fm=Registration(instance=pi)
    return render(request,'level/Update.html',{'form':fm})

def Conform(request):
    return render(request,'level/Conform_delete.html')

def Python(request):
    return render(request,'level/Python.html')

def Aws(request):
    return render(request,'level/Aws.html')

def Devops(request):
    return render(request,'level/Devops.html')

def Java(request):
    return render(request,'level/Java.html')

def Cloud(request):
    return render(request,'level/Cloud.html')