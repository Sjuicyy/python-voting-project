from http.client import HTTPResponse
from django.shortcuts import render
from django.http  import htt

# Create your views here.

def index(request):
    return HTTPResponse("hello world . You're at the polls index.")

