from django.shortcuts import render


def index(request):
    return HttpResponse('<h1>Alura Space</h1><p>Bem vindo ao espaço!')
