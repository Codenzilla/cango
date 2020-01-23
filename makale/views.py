from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import MakaleForm
from .models import Makale, Comment
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
# Create your views here.

def makale(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Makale.objects.filter(baslik__contains = keyword)
        return render(request,"articles.html",{"articles":articles})

    articles = Makale.objects.all()
    return render(request,"articles.html",{"articles":articles})

def index(request):
    context = {
        "bir" : "Hele hele",
        "iki" : "Zamazink",
        "üç" : [1,2,3,4,5]
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def detail(request,id):
    return HttpResponse("Detail "+str(id))

@login_required(login_url = "user:loginUser")
def dashboard(request):
    makaleler = Makale.objects.filter(yazar = request.user)
    context = {
        "makaleler":makaleler
    }
    return render(request, "dashboard.html",context)

@login_required(login_url = "user:loginUser")
def makaleekle(request):
    form = MakaleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        makale = form.save(commit = False)
        makale.yazar = request.user
        makale.save()
        messages.success(request,"Makale oluşturuldu")
        return redirect("makale:dashboard")
    return render(request,"makaleekle.html",{"form":form})

def detail(request,id):
    makaleler = get_object_or_404(Makale, id=id)

    comments = makaleler.comments.all()

    return render(request, "detail.html",{"makaleler":makaleler,"comments":comments})

@login_required(login_url = "user:loginUser")
def updateArticle(request,id):
    article = get_object_or_404(Makale, id = id)
    form = MakaleForm(request.POST or None, request.FILES or None, instance = article)

    if form.is_valid():
        article = form.save(commit=False)
        article.yazar = request.user
        article.save()

        messages.success(request,"Makale Guncellendi")
        return redirect("makale:dashboard")

    return render(request, "update.html", {"form":form})

@login_required(login_url = "user:loginUser")
def deleteArticle(request,id):
    article = get_object_or_404(Makale, id = id)
    article.delete()

    messages.success(request,"Sildik")

    return redirect("makale:dashboard")

def addComment(request, id):
    article = get_object_or_404(Makale,id=id)
    
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author = comment_author, comment_content = comment_content)

        newComment.article = article

        newComment.save()
    
    return redirect(reverse("makale:detail", kwargs={"id":id}))
    