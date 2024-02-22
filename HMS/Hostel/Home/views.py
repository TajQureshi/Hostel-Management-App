from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def Home(request):
    return render(request, 'Home/base.html')


def Signup(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(email__iexact = email).exists():
            user = User.objects.create_user(first_name=fname, last_name=lname, email=email, username=username, password=password)
            user.save()
            messages.success(request, "User Added Successfully!!!")
            return redirect('/signin')
        else:
            messages.error(request, "Email already Exist!!!")

    return render(request, 'Home/signup.html')


def Signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # return redirect('/')
            return redirect(request.GET.get('next', '/'))
        
        else:
            messages.error(request, "Wrong Access Credentials.....")

    return render(request, 'Home/signin.html')


def Signout(request):
    logout(request)
    return redirect('/')


@login_required(login_url="/signin")
def Book_Bed(request):
    beds = Bed.objects.filter(status=False)
    
    if request.method == "POST":
        bed_id = request.POST.get('bed')
        bd = Bed.objects.get(id=bed_id)

        date = request.POST.get('date')

        Booking.objects.create(bed=bd, user=request.user, date=date)
        bd.status = 'True'
        bd.save()

        messages.success(request, "Your Booking is Confirmed!!")

    bd = Bed.objects.all()
    context = {'beds':beds, 'bd':bd}
    return render(request, 'Home/booking.html', context)


@login_required(login_url="/signin")
def Account(request):
    books = Booking.objects.filter(user=request.user)
    return render(request, 'Home/account.html', {'books':books})

