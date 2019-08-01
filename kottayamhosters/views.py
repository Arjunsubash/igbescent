from django.shortcuts import render, redirect
from kottayamhosters.form import Message_data, Logo_data, video_data,\
    design_data, Loginform, printart_data
from django.core.mail import send_mail
from django.conf import settings
from django.urls.base import reverse
from kottayamhosters.models import Add_logo, Add_video, Add_design, Add_printart
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.

def form_login(request):
    if request.method == "POST":
        form = Loginform(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                    login(request,user)
                    return redirect('devhome') 
            else:
                    messages.info(request, 'LOGIN  FAILED')
                    return render(request, 'pages-login.html',{'form' : form})
        else:
                messages.info(request, 'LOGIN  FAILED')
                return render(request, 'pages-login.html',{'form' : form})       
        
    else:    
        form = Loginform()
        return render(request, 'pages-login.html',{'form' : form})
def Home(request):
    if request.method == "POST":
        form=Message_data(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['name']
            Email_data = form.cleaned_data['Email_field']
            phone_number = str(form.cleaned_data['Phno'])
            message_data = form.cleaned_data['Text_area']
            message = "Name : "+subject + "\nEmail :"+Email_data + "\nPhone number :"+phone_number + "\nMessage :"+message_data
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['ignescenttechnologies@gmail.com',]
            send_mail( subject, message, email_from, recipient_list,fail_silently=False )
            return redirect('home')
        else:
            return render(request,'Home.html',{'form':form})
    else:
        form=Message_data()
        logo_dis = Add_logo.objects.all()
        video_dis = Add_video.objects.all()
        design_dis = Add_design.objects.all()
        printart_dis = Add_printart.objects.all()
        return render(request,'Home.html',{'form':form, 'logo_dis':logo_dis, 'video_dis':video_dis, 'design_dis':design_dis, 'printart_dis':printart_dis})

@login_required(login_url='/ignescent/')
def dev_home(request):
    return render(request,'add_home.html')
@login_required(login_url='/ignescent/')    
def add_logo(request):
    if request.method == "POST":
        form = Logo_data(request.POST,request.FILES) 
        if form.is_valid():
            form.save()
            return  redirect('devhome')
        
        else:
            logo_form = Logo_data()
            return render(request,'logodesign.html',{'logo_form':logo_form})
    else:
        logo_form = Logo_data()    
        logo_data = Add_logo.objects.all()
        return render(request,'logodesign.html',{'logo_form':logo_form, 'logo_data' : logo_data})
@login_required(login_url='/ignescent/')
def add_video(request):
    if request.method == "POST":
        video_form = video_data(request.POST,request.FILES) 
        if video_form.is_valid():
            video_form.save()
            return  redirect('devhome')
    else:
        video_form = video_data()
        return render(request,'videoedit.html',{'video_form':video_form})
@login_required(login_url='/ignescent/')
def add_design(request):
    if request.method == "POST":
        design_form = design_data(request.POST,request.FILES) 
        if design_form.is_valid():
            design_form.save()
            return  redirect('devhome')
    design_form = design_data()
    return render(request,'webdesign.html',{'design_form':design_form})
@login_required(login_url='/ignescent/')
def add_printart(request):
    if request.method == "POST":
        printart_form = printart_data(request.POST,request.FILES) 
        if printart_form.is_valid():
            printart_form.save()
            return  redirect('devhome')
    printart_form = printart_data()
    return render(request,'printart.html',{'printart_form':printart_form})
def form_logout(request):   
    logout(request)
    return redirect('home')
    
    
    
    