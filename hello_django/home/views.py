from django.shortcuts import render


def home(request):

    context = {
        'text': 'Olá home'
    }

    print('HOME')
    # RENDER ---> busca arquivos dos diretórios: TEMPLATES e BASE
    return render(
        request,
        'home/index.html',  # Busca automaticamente todos os arquivos que estão dentro da pasta TEMPLATES na raiz da pasta do APP
        context,
    )