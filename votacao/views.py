from django.core.paginator import Paginator
from django.forms import modelformset_factory
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView

from .forms import *
from .models import *


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    
    paginator = Paginator(latest_question_list, 4)
    page = request.GET.get('page')
    
    latest_question_list = paginator.get_page(page)
    
    busca = request.GET.get('termo')
    if busca:
        latest_question_list = Question.objects.filter(question_text__icontains = busca)
    
    context = {'latest_question_list': latest_question_list}
    return render(request, 'votacao/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except:
        raise Http404("Question does not exist")
    
    context = {'question': question}
    return render(request, 'votacao/detail.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'votacao/results.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        print(selected_choice)
        
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'votacao/detail.html', {'question': question, 'error_message': "Você não selecionou nenhuma opção.",})
    
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse('votacao:results', args=(question.id, )))    


class DispatchLoginRequiredMixin(View):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('perfil:login')

        return super().dispatch(*args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(usuario=self.request.user)
        return qs


class PollsCreateView(DispatchLoginRequiredMixin, CreateView):
    form_class = PollsForm
    template_name = 'votacao/addPolls.html'
    
    def get_context_data(self, **kwargs):
        context = super(PollsCreateView, self).get_context_data(**kwargs)
        
        context['choice_meta_formset'] = ChoiceMetaInLineFormset()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = None
        # form_class = self.get_form_class()
        form = self.get_form()
        choice_meta_formset = ChoiceMetaInLineFormset(self.request.POST)
        
        if form.is_valid() and choice_meta_formset.is_valid():
            self.form_valid(form, choice_meta_formset)
            return redirect('votacao:index')
        else:
            return redirect('votacao:addPolls')
    
    def form_valid(self, form, choice_meta_formset):
        choice_metas = choice_meta_formset.save(commit=False)
        
        if len(choice_metas) < 2:
            print('Adicionar mensagem informando ao usuário que a enquete dele nao foi salva')
            return
            
        self.object = form.save(commit=False)
        self.object.save()
        
        #saving choice instances
        for meta in choice_metas:
            meta.question = self.object
            meta.save()
        
        return redirect(reverse('votacao:addPolls'))
    
    def form_invalid(self, form, choice_meta_formset):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                choice_meta_formset = choice_meta_formset
            )
        )
