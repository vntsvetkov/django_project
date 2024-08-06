from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from .models import Post
from copy import deepcopy


# Create your views here.
def main(request: HttpRequest):

    posts = Post.objects.all()

    best_posts = Post.objects.order_by('rating')

    context = {
        'posts': posts,
        'best_posts': best_posts[:2],
    }

    return render(request, 'posts.html', context=context)


def redirect(request: HttpRequest):
    return render(request, '404.html')

