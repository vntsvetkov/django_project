from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect


# Create your views here.
def main(request: HttpRequest):
    return render(request, 'posts.html')


def redirect(request: HttpRequest):
    return HttpResponseRedirect('/blog/')

