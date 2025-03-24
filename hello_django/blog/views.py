# from django.http import HttpResponse
from django.shortcuts import render

def blog(request):
    print('blog')

    context = {
        'text': 'Olá blog',
        'title': 'Essa é uma pagina de exemplo - '
    }


    return render(
        request,
        'blog/index.html',
        context,
    )

def exemplo(request):

    context = {
        'text': 'Olá exemplo ',
        'title': 'Essa é uma pagina de exemplo - '
    }
    
    print('exemplo')
    return render(
        request,
        'blog/exemplo.html',
        context,
    )