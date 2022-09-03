from django.shortcuts import redirect, render
from .models import *
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password, make_password
# Create your views here.

def first_page(request):

    return render(request, 'index.html')

def sign_ups(request):
    if request.method =="POST":
        sign_name = request.POST.get('name')
        sign_email = request.POST.get('email')
        sign_password = request.POST.get('password')
        sign_phone = request.POST.get('phone')
        data = sign_up(name = sign_name, email = sign_email, password =make_password(sign_password), number = sign_phone)
        data.save()
    return HttpResponse('Data submit success')

def login(request):
    if request.method =="POST":
        sign_email = request.POST.get('email')
        sign_password = request.POST.get('password')
        try:
            fetch_info = sign_up.objects.get(email = sign_email)
            if (check_password(sign_password, fetch_info.password)):

                request.session['name'] = fetch_info.name
                request.session['email'] =fetch_info.email
                return redirect("index")
            else :
                return HttpResponse("please enter valid password")

        except :
            return HttpResponse("please enter a valid email")

def logout(request):
    request.session.clear()
    return redirect('index')


def logsin(request):
    return render(request, 'login.html')