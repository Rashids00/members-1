from django.shortcuts import render
from django.http import HttpResponse

def project1(request):
    return HttpResponse("New Project")