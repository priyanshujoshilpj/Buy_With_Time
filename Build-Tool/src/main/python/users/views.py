from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import UserModel



# Create your views here.
def home(request):
    return render(request, "users/index.html")

def signup(request):
    
    if request.method == "POST":
        #username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

      
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        user_ins = UserModel(fname=fname,lname=lname,email=email,pass1=pass1)

        myuser.save()
        user_ins.save()
        

        messages.success(request, "Your Account has been successfully created.")

        return redirect('signin')

    return render(request, "users/signup.html")

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "users/index.html", {'fname': fname})

        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')


    return render(request, "users/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Succefully!")
    return redirect ('home')

def aboutus(request):
    return render(request, "users/aboutus.html")

def contactus(request):
    return render(request, "users/contactus.html")