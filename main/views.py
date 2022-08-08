from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import ContatoForm


class MainView(TemplateView):
    template_name = 'main/mainIndex.html'


class SobreView(TemplateView):
    template_name = 'main/sobre.html'
    
    
def contato(request):
    if str(request.method) == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            #chamando método de envio de email
            form.send_email()
            messages.success(request, 'Email enviado com sucesso.')
            form = ContatoForm()
        else:
            messages.error(request, 'Email NÃO FOI enviado com sucesso.')
    else:
        form = ContatoForm()
    
    context = {
        'form':form
    }
    return render(request, 'main/sobre.html', context)
    
