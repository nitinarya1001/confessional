from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        "var1" : "This is a bruh"
    }
    return render( request, "index.html", context)

def about(request):    
    context={
        "var1" : "This is a ABOUTPAGE"
    }
    return render(request, "index.html", context)
