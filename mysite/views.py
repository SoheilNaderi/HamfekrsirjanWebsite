
from django.http import HttpResponse,JsonResponse

def home(request):
    return HttpResponse('ckfdskfsdfksd fu')

def jsontest(request):
    return JsonResponse({'name':'soheil'})