from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

def home(request):
    return HttpResponse('<h1> HI WELCOME TO MY SITE <h1>')
def contact(request):
    return HttpResponse('<h1>contact<h1>')

def about(request):
    return HttpResponse('<h1>about<h1>')

def jsontest(request):
    return JsonResponse({'name':'soheil'})

