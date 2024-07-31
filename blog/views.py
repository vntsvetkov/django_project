from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from .models import Post


# Create your views here.
def main(request: HttpRequest):

    # p = Post(title='Новость 2', text='Текст новости 2', author='Петров А.', publish_date='2024-07-31')
    # p.save()

    posts = Post.objects.values()
    posts = posts.filter(publish_date='2024-07-31')

    context = {
        'posts': posts
    }

    return render(request, 'posts.html', context=context)


def redirect(request: HttpRequest):
    return render(request, '404.html')

