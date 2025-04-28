from django.shortcuts import render
from datetime import datetime
from .models import confessions, contact

DATA = confessions.objects.all()
# Create your views here.
def index(request):
    context={
        "title" : "Confessional",
        "data" : DATA
    }
    
    return render( request, "index.html", context)

def confession(request):
    context={
        "title" : "blog" #change it with the title of confession
    }    
    return render( request, "confessionPage.html", context)
        

def confess(request):    
    context={
        "title" : "Confess"
    }
    if(request.method == 'POST'):
        title = request.POST.get('title')
        confession = request.POST.get('confession')
        confessionInstance = confessions(title=title, confession=confession)
        confessionInstance.save()
        
    return render(request, "confess.html",context)

def aboutus(request):  
    context={
        "title" : "About Us"
    }  
    return render(request, "aboutus.html",context)

def contactus(request): 
    context={
        "title" : "Contact Us"
    }   
    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contactInstance = contact(name=name, email=email, message=message , date = datetime.now())
        contactInstance.save()
        
    return render(request, "contactus.html",context)
