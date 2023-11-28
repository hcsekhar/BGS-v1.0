from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(req):
    return render(req,'home.html')

def about(req):
    return render(req,'about.html')


def product(req):
    return render(req,'product_design.html')

def web(req):
    return render(req,'web_design.html')

def Digital(req):
    return render(req,'Digital_market.html')
    
def mobile(req):
    return render(req,'mobile_app.html')

def staff(req):
    return render(req,'it_staff.html')

def blog(req):
    return render(req,'blog.html')

def port(req):
    return render(req,'portfolio.html')

def team(req):
    team = Team.objects.all()
    return render(req,'teams.html', {'team':team})

def  gallery(req,pid):
     if pid == 0:
        gallery = Gallery.objects.all()
     else:
        category = Category.objects.get(id=pid)
        gallery = Gallery.objects.filter(category=category)
     allcategory = Category.objects.all()
     return render(req,'gallery.html',locals())

def  contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name,email=email,message=message)
        return redirect(home)
    return render(request,'contact.html')