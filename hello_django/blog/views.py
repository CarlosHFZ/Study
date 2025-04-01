# from django.http import HttpResponse
from django.shortcuts import render
from blog.data import posts

def blog(request):
    print('blog')

    context = {
        # 'text': 'Olá blog',
        'title': 'Página - ',
        'posts': posts
    }


    return render(
        request,
        'blog/index.html',
        context,
    )

def exemplo(request):

    context = {
        'text': 'Olá exemplo ',
        'title': 'Página - '
    }
    
    print('exemplo')
    return render(
        request,
        'blog/exemplo.html',
        context,
    )