from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Notes

# Create your views here.
def home(request):
    note1 = Notes.objects.all()
    return render(request, 'index.html', {'note1':note1})

def register(request):
    if request.method == 'POST':
        user = request.POST["Username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password1 = request.POST["password1"]
        if password != password1:
            messages.info(request, "Password do not match")
            return redirect("/register")
        else:
            if User.objects.filter(username=user).exists():
                messages.info(request, "Username already exsit")
                return redirect("/register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exsist")
                return redirect("/register")
            else:
                user = User.objects.create_user(username=user, email=email, password = password)
                user.save()
                messages.info(request, "User has been successfully created")
                return redirect("/login")
    else:    
        return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        user = request.POST["user"]
        password1 = request.POST["password"]     
        t1 = auth.authenticate(username=user, password=password1)
        if t1 is not None:
            auth.login(request, t1)
            return redirect("/")
        else:
            messages.info(request, "Invalid username or password")
            return redirect("/login")
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect("/")
def add_note(request):
    if request.method=="POST":
        title = request.POST["title"]
        desc = request.POST["descrip"]
        note = Notes(title=title, description=desc)
        note.save()
        messages.info(request, "Note added succesfully")
        return redirect("/")
    else:
        return render(request, "notes.html")