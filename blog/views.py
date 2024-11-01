from django.shortcuts import render
from .models import Post, Blog, Mensagem

def index(request):
    context = {
        "posts": Post.objects.all(),
        "blog": Blog.objects.first()
    }
    return render(request, "index.html", context)

def post(request, post_id):
    context = {
        "post": Post.objects.get(pk=post_id),
    }
    return render(request, "post.html", context)

def sobre(request):
    context = {
        "blog": Blog.objects.first(),
    }
    return render(request, "sobre.html", context)

def contato(request):
    if request.method == "POST":
        print(request.POST('nome'))
        print(request.POST('email'))
        print(request.POST('telefone'))
        print(request.POST('mensagem'))

        return render(request, "contato.html", context)
    else:
        context = {
            "blog": Blog.objects.first(),
        }
        return render(request, "contato.html", context)