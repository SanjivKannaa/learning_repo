from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def detail(request, question_id):
    return HttpResponse("this is the detail view of the question: ".format(question_id))

def results(request, question_id):
    return HttpResponse("these are the result of the question: ".format(question_id))

def error_500(request):
    data = {}
    return render(request, '500.html', data)

