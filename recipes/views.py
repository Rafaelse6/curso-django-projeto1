from django.http import HttpResponse


def home(request):
    return HttpResponse('HOME 1')


def contato(request):
    return HttpResponse('contato 2')


def sobre(request):
    return HttpResponse('sobre 2')
