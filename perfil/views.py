from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from perfil.forms import createUserForm


def loginPage(request):
    if request.user.is_authenticated:
        messages.add_message(
            request,
            messages.WARNING,
            'Você já se encontra logado.'
        )
        return redirect('votacao:index')
    
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    f'Bem vindo {username}, você agora está logado.'                    

                )
                return redirect('votacao:index')
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Ooops... Usuário ou senha estão inválidos.'                    
                )                
        
        context = {}
        return render(request, 'perfil/login.html', context)


def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.add_message(
            request,
            messages.WARNING,
            f'Usuário foi deslogado com sucesso.'
        )
        return redirect('votacao:index')
    else:        
        return redirect('votacao:index')


def registerPage(request):
    if request.user.is_authenticated:
        messages.add_message(
            request,
            messages.WARNING,
            f'Você já se encontra logado.'
        )
        return redirect('votacao:index')
    
    else:
        form = createUserForm()
        
        if request.method == 'POST':
            form = createUserForm(request.POST)
            
            if form.is_valid():
                user = form.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Você agora pode realizar o seu login.'
                )
                return redirect('perfil:login')
            
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Ooops... você digitou algum campo inválido.'
                )
    
    context = {'form': form}
    return render(request, 'perfil/register.html', context)
