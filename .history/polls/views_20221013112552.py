from http.client import HTTPResponse
from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hello world . You're at the polls index.")

def detail (request,question_id):
    return HttpResponse("you're looking at question %s" % question id)

def result(request,question_id)