from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        "title" : "Confessional"
    }
    return render( request, "index.html", context)

def confess(request):    
    context={
        "title" : "Confess"
    }
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
    return render(request, "contactus.html",context)
