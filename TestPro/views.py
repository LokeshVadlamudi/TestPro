from django.shortcuts import render


def onLoad(request):
    return render(request, 'base.html')


def login(request):
    return render(request, 'login.html')

