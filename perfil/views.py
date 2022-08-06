from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from perfil.forms import createUserForm


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('votacao:index')
    
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('votacao:index')
        
        context = {}
        return render(request, 'perfil/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('votacao:index')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('votacao:index')
    
    else:
        form = createUserForm()
        
        if request.method == 'POST':
            form = createUserForm(request.POST)
            
            if form.is_valid():
                user = form.save()
                return redirect('perfil:login')
    
    context = {'form': form}
    return render(request, 'perfil/register.html', context)
    
    
    
    context = {}
    return render(request, 'perfil/register.html', context)
