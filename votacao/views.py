from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .models import *


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    
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
