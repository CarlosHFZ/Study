# from django.http import HttpResponse
from django.shortcuts import render
from blog.data import posts
from typing import Any
from django.http import HttpRequest, Http404


def blog(request):
    print('blog')

    context = {
        # 'text': 'Olá blog',
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
    }
    
    print('exemplo')
    return render(
        request,
        'blog/exemplo.html',
        context,
    )


def post(request: HttpRequest, post_id: int):
    print('post', id)
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe.')

    context = {
        # 'text': 'Olá post',
        'post': found_post,
        'title': found_post['title'] + ' - ',
    }

    return render(
        request,
        'blog/post.html',
        context,
    )
