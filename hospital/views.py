from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import  *
from .utils import  *


# Get the Django's built-in User Model

User=get_user_model()
# Create your views here.

def login_view(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")

        user=authenticate(request,username=email,password=password)
        if user != None:
            login(request,user)
            return redirect("home")
        else:
            return redirect("login")
    else:


        return render(request,"pages-login.html")

def register(request):
    if request.method== "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        number=request.POST.get("number")
        password=request.POST.get("password")

        user=User.objects.create_user(username=email,password=password)
        ProfileModel.objects.create(user=user,name=name,contact=number,email=email)
        return redirect("login")


    else:
        
        return render(request,"pages-register.html")



def logout_view(request):
    logout(request)
    #redirect function takes the url name not the function name
    return redirect("login")


@login_required(login_url="login")
def doc_manage(request):
    if request.method == "POST":

        #Adding Function
        name=request.POST.get("name")
        specialization=request.POST.get("special")
        fees=request.POST.get("fees")
        days=request.POST.get("days")
        contact=request.POST.get("number")

        if days==0:
            status="Not Avalibale"
        else:
            status="Avaliable"

        user=User.objects.get(id=request.user.id)
        doctor=DoctorModel.objects.create(user=user,name=name,specialization=specialization,fees=fees,days=days,contact=contact,status=status)

        return redirect("doc_manage")

    else:
        user=User.objects.get(id=request.user.id)
        doc=DoctorModel.objects.filter(user=user)

        profile=ProfileModel.objects.get(user=user)

        try:
            img=profile.profile_pic.url
        except:
            img=None
        
        return render(request,"doc_manage.html",{"doc":doc,"img":img,"prof":profile})


@login_required(login_url="login")
def home(request):

    user=User.objects.get(id=request.user.id)
    profile=ProfileModel.objects.get(user=user)

    try:
        img=profile.profile_pic.url
    except:
        img=None
    return render(request,"index.html",{"img":img,"prof":profile})

@login_required(login_url="login")
def doc_view(request,id):
    doc_info=DoctorModel.objects.get(id=id)

    user=User.objects.get(id=request.user.id)
    profile=ProfileModel.objects.get(user=user)

    try:
        img=profile.profile_pic.url
    except:
        img=None

    return render(request,"view_doc.html",{"doc":doc_info,"img":img,"prof":profile})

@login_required(login_url="login")    
def pat_manage(request):
    if request.method == "POST":
        name=request.POST.get("name")
        age=request.POST.get("age")
        address=request.POST.get("address")
        number=request.POST.get("number")

        user=User.objects.get(id=request.user.id)
        patient=PatientModel.objects.create(user=user,name=name,age=age,address=address,contact=number)
        return redirect("pat_manage")
    else:
        user=User.objects.get(id=request.user.id)
        pat=PatientModel.objects.filter(user=user)


        user=User.objects.get(id=request.user.id)
        profile=ProfileModel.objects.get(user=user)

        try:
            img=profile.profile_pic.url
        except:
            img=None
        return render(request,"pat_manage.html",{"pat":pat,"img":img,"prof":profile})

@login_required(login_url="login")    
def pat_view(request,id):
    pat_info=PatientModel.objects.get(id=id)

    user=User.objects.get(id=request.user.id)
    profile=ProfileModel.objects.get(user=user)

    try:
        img=profile.profile_pic.url
    except:
        img=None
    return render(request,"view_pat.html",{"pat": pat_info,"img":img,"prof":profile})

@login_required(login_url="login")
def doc_edit(request,id):
    if request.method=="POST":
        name=request.POST.get("name")
        specialization=request.POST.get("special")
        fees=request.POST.get("fees")
        days=request.POST.get("days")
        contact=request.POST.get("number")

        if days==0:
            status="Not Avalibale"
        else:
            status="Avaliable"

        doc=DoctorModel.objects.get(id=id)
        doc.name=name
        doc.specialization=specialization
        doc.fees=fees
        doc.days=days
        doc.contact=contact
        doc.status=status
        doc.save()

        return redirect("doc_manage")


    else:
        doc=DoctorModel.objects.get(id=id)
        user=User.objects.get(id=request.user.id)
        profile=ProfileModel.objects.get(user=user)

        try:
            img=profile.profile_pic.url
        except:
            img=None

        return render(request,"edit_doc.html",{"doc":doc,"img":img,"prof":profile})

@login_required(login_url="login")
def pat_edit(request,id):
    if request.method=="POST":
        name=request.POST.get("name")
        age=request.POST.get("age")
        address=request.POST.get("address")
        number=request.POST.get("number")

        pat=PatientModel.objects.get(id=id)
        pat.name=name
        pat.age=age
        pat.address=address
        pat.number=number
        pat.save()

        return redirect("pat_manage")

    else:
        pat=PatientModel.objects.get(id=id)

        user=User.objects.get(id=request.user.id)
        profile=ProfileModel.objects.get(user=user)

        try:
            img=profile.profile_pic.url
        except:
            img=None

        return render(request,"edit_pat.html",{"pat":pat,"img":img,"prof":profile})

@login_required(login_url="login")
def apot_manage(request):
    if request.method == "POST":
        pat_id=request.POST.get("pat_name")
        doc_id=request.POST.get("doc_name")
        date=request.POST.get("date")
        time=request.POST.get("time")
        email=request.POST.get("email")
        
    
        user=User.objects.get(id=request.user.id)
        doc=DoctorModel.objects.get(id=doc_id)
        pat=PatientModel.objects.get(id=pat_id)



        if doc.days>0:
            
            apot=AppointmentModel.objects.create(user=user,doctor=doc,patient=pat,date=date,time=time,email=email)
            appoinment_email(email,apot)
            doc.days-=1

            if doc.days==0:
                status="Not Avalibale"
            else:
                status="Avaliable"
            doc.status=status
            doc.save()

            return redirect ("apot_manage")
        else:
            messages.error(request, f"No Appointment available for Dr. {doc.name}")
            return redirect ("apot_manage")
        
    else:
        user=User.objects.get(id=request.user.id)
        doc=DoctorModel.objects.filter(user=user)
        pat=PatientModel.objects.filter(user=user)
        apot=AppointmentModel.objects.filter(user=user)

        user=User.objects.get(id=request.user.id)
        profile=ProfileModel.objects.get(user=user)

        try:
            img=profile.profile_pic.url
        except:
            img=None
        return render(request,"apot_manage.html",{"pat":pat,"doc":doc,"apot":apot,"img":img,"prof":profile})

@login_required(login_url="login")
def apot_view(request,id):
    apot_info=AppointmentModel.objects.get(id=id)

    user=User.objects.get(id=request.user.id)
    profile=ProfileModel.objects.get(user=user)

    try:
        img=profile.profile_pic.url
    except:
        img=None
    return render(request,"view_apot.html",{"apot":apot_info,"img":img,"prof":profile})

@login_required(login_url="login")
def apot_edit(request,id):
    if request.method== "POST":
        date=request.POST.get("date")
        time=request.POST.get("time")

        apot=AppointmentModel.objects.get(id=id)
        apot.date=date
        apot.time=time
        apot.save()
        return redirect("apot_manage")
    else:
        apot_info=AppointmentModel.objects.get(id=id)

        user=User.objects.get(id=request.user.id)
        profile=ProfileModel.objects.get(user=user)

        try:
            img=profile.profile_pic.url
        except:
            img=None

        return render(request,"edit_apot.html",{"apot":apot_info,"img":img,"prof":profile})

@login_required(login_url="login")
def doc_del(request,id):
    doc=DoctorModel.objects.get(id=id)
    doc.delete()
    return redirect("doc_manage")

@login_required(login_url="login")
def pat_del(request,id):
    pat=PatientModel.objects.get(id=id)
    pat.delete()
    return redirect("pat_manage")

@login_required(login_url="login")
def apot_done(request,id):
    apot=AppointmentModel.objects.get(id=id)

    doc=apot.doctor
    pat=apot.patient
    date=apot.date
    time=apot.time
    email=apot.email


    user=User.objects.get(id=request.user.id)
    apot_done=Appointment_done_Model.objects.create(user=user,doctor=doc,patient=pat,date=date,time=time,email=email)

    doctor=DoctorModel.objects.get(id=doc.id)
    doctor.days+=1

    if doctor.days==0:
        status="Not Avalibale"
    else:
         status="Avaliable"
    doctor.status=status
    doctor.save()
    apot.delete()
    return redirect("apot_manage")

@login_required(login_url="login")
def profile(request):
    user=User.objects.get(id=request.user.id)
    profile=ProfileModel.objects.get(user=user)

    try:
        img=profile.profile_pic.url
    except:
        img=None
    return render(request,"prof.html",{"prof":profile , "img":img})

def updt_prof(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        contact=request.POST.get("contact")
        address=request.POST.get("name")

        pic=request.FILES.get("pic")

        user=User.objects.get(id=request.user.id)
        prof=ProfileModel.objects.get(user=user)

        prof.name=name
        prof.email=email
        prof.contact=contact
        prof.address=address
        prof.profile_pic=pic
        prof.save()

        return redirect("profile")
        