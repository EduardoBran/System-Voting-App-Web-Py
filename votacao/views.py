from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import *


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    
    paginator = Paginator(latest_question_list, 4)
    page = request.GET.get('page')
    
    latest_question_list = paginator.get_page(page)
    
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
