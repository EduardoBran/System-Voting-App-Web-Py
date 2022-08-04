from django.shortcuts import render

from .models import *


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    
    context = {'latest_question_list': latest_question_list}
    return render(request, 'votacao/index.html', context)


def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    context = {'question': question}
    return render(request, 'votacao/detail.html', context)



def results(request, question_id):
    question = Question.objects.get(pk=question_id)
    context = {'question': question}
    return render(request, 'votacao/results.html', context)
