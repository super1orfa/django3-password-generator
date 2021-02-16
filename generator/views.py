import random
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_page(request):

    return render(request, "generator/home.html")


def password_page(request):
    generatedpassword = ""
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*()_+|'))

    length = int(request.GET.get('length', 12))

    for x in range(length):
        generatedpassword += random.choice(characters)

    context = {
        "password": generatedpassword
    }
    return render(request, "generator/password.html", context)


def about_page(request):
    context = {
        "about":"This is About Page"
    }
    return render(request,"generator/about_page.html",context)