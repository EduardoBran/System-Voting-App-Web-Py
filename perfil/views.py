from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render


def loginPage(request):
    return render(request, 'perfil/login.html')

