from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail( request, question_id) :
    return HttpResponse("Você está procurando pela questão %s." %question_id)

def results(request, question_id) :
    response = "Você está procurando pelos resultados da questão %s."
    return HttpResponse(response % question_id)

def vote( request, question_id) :
    return HttpResponse( "Você está votando na questão %s." %question_id)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})