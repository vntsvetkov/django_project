from django.urls import path
from personal.views import main

urlpatterns = [
    path('', main),
]