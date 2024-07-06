from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect


# Create your views here.
def main(request: HttpRequest):
    return render(request, 'mybooks.html')


def redirect(request: HttpRequest):
    return render(request, '404.html')

