from django.shortcuts import render, HttpResponse
# esse render é p redenrizar no html
# httpresponde vai interpretar oq eu colocar como parametro e vai jogar como resposta http

# Create your views here.

# def hello(request): # parametro é request q é a requisição, q são os dados a serem enviados
#     return HttpResponse('<h1>Hello World<h1>')

# def hello(request, nome): # mais de um parametro
#     return HttpResponse('<h1>Hello {}<h1>'.format(nome))

def hello(request, nome, idade): # mais de 2 parametros
    return HttpResponse('<h1>Hello {} de {} anos <h1>'.format(nome,idade))