from django.http import HttpResponse
from django.shortcuts import redirect, render

from home.models import *

# Create your views here.
def signup(request):
    if request.method == "POST":
        number = request.POST['number']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        data = userdata(number=number, email = email, firstname=firstname, lastname=lastname, password=password)
        data.save()
        return redirect("/")
    return render(request, "fk_signup.html")

def login(request):
    if request.method == "POST":
        number = request.POST.get('number')
        password = request.POST.get('password')
        

        if userdata.objects.filter(number = number, password=password).exists():
            return redirect("/index")
        else:
            return render(request, "error.html")

    return render(request, "fk_login.html")

def index(request):
    allproduct = product.objects.all()
    params = {'allproduct': allproduct}
    return render(request, "fk-index.html", params)
    
