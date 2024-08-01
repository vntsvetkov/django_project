from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from .models import Post


# Create your views here.
def main(request: HttpRequest):

    posts = Post.objects.values()
    print(posts)
    context = {
        'posts': posts
    }

    return render(request, 'posts.html', context=context)


def redirect(request: HttpRequest):
    return render(request, '404.html')

