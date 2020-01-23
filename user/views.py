from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def register(request):

    form = RegisterForm(request.POST or None) #Bu b satır aşşaki şiyleri kapsıyo
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser),
        messages.info(request,"Kaydoldun geç")

        return redirect("index")

    context = {"form" : form,}
    return render(request,"register.html", context)

    """if request.method == "POST":
        context = {"form" : form,}
        return render(request,"register.html", context)
    else:
        form = RegisterForm()
        context = {"form" : form}
        return render(request,"register.html", context)"""

def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form" : form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username= username, password = password)

        if user == None:
            messages.info(request,"Kullanıcı adı veya parola hatıalı")
            return render(request, "login.html", context)
        
        messages.success(request, "İçerdesin evlat")

        login(request,user)
        return redirect("index")

    return render(request, "login.html", context)

    return render(request,"login.html")

def logoutUser(request):
    logout(request)
    messages.success(request,"Çehdi Gitti")
    return redirect("index")