from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Notes

# Create your views here.
def home(request):
    note1 = Notes.objects.filter(user=request.user.username)
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
                messages.info(request, "Username already exist")
                return redirect("/register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exist")
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
        note = Notes(user = request.user.username,title=title, description=desc)
        note.save()
        messages.info(request, "Note added succesfully")
        return redirect("/")
    else:
        return render(request, "notes.html")

def delete(request, id):
    t1 = Notes.objects.get(id=id)
    t1.delete()
    return redirect("/")

def edit(request, id):
    t1 = Notes.objects.get(id=id)
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['des']
        t1.title = title
        t1.description = desc
        t1.save()
        messages.info(request, "Note edited successfully")
        return redirect("/")
    else:
        return render(request, "edit.html", {"id1": t1})
def delete_account(request):
    username = request.user.username
    auth.logout(request)
    user = User.objects.get(username=username)
    notes = Notes.objects.filter(user = username)
    for i in notes:
        i.delete()
    user.delete();
    messages.info(request, "Account deleted succesfully")
    return redirect("/login")