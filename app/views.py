from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html',{'nav':'index'})

def about(request):
    return render(request,'about.html',{'nav':'about'})

def blog(request):
    return render(request,'blog.html',{'nav':'blog'})

def cart(request):
    return render(request,'cart.html',{'nav':'cart'})

def checkout(request):
    return render(request,'checkout.html',{'nav':'checkout'})

def contact(request):
    return render(request,'contact.html',{'nav':'contact'})

def services(request):
    return render(request,'services.html',{'nav':'services'})

def shop(request):
    return render(request,'shop.html',{'nav':'shop'})

def thankyou(request):
    return render(request,'thankyou.html',{'nav':'thankyou'})