from base64 import urlsafe_b64encode
from email.message import EmailMessage
from encodings import utf_8
from lib2to3.pgen2.tokenize import generate_tokens
from telnetlib import LOGOUT
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from events import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from . tokens import generate_token
# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def dashboard(request):
    return render(request, "authentication/dashboard.html")

def about(request):
    return render(request, "authentication/about.html")

def index(request):
    return render(request, "authentication/index.html")

def contact(request):
    return render(request, "authentication/contact.html")

def BuyNow(request):
    return render(request, "authentication/BuyNow.html")

def Rent(request):
    return render(request, "authentication/Rent.html")

def dashboard(request):
    return render(request, "authentication/dashboard.html")

def Logout(request):
    return render(request, "authentication/index.html")

def signup(request):
    if request.method == "POST":
        #username = request.POST.get("username")
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists! Please try another username")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('home')
        
        if len(username)>10:
            messages.error(request, "Username must be under 10 characters")

        if pass1 != pass2:
            messages.error(request, "Password didn't match!")

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()

        messages.success(request, "Your Account has been successfully created.")
        





    return render(request, "authentication/signup.html")

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']


        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            fname = user.first_name 
            return render(request, "authentication/dashboard.html", {'fname': fname})

        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')


'''def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')

    else:
        return render(request, 'activation_failed.html')'''
