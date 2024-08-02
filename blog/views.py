from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from .models import Post
from copy import deepcopy


# Create your views here.
def main(request: HttpRequest):

    posts = Post.objects.all()
    best_posts = deepcopy(posts)

    # Запросить все теги связанные с постом

    posts_id = Post.objects.values('id')

    tags_dict = {}
    for d in posts_id:
        tags = Post.objects.get(id=d['id']).tags.all()
        tags_dict[d['id']] = tags

    context = {
        'posts': posts,
        'best_posts': best_posts,
        'tags': tags_dict,
    }

    return render(request, 'posts.html', context=context)


def redirect(request: HttpRequest):
    return render(request, '404.html')

