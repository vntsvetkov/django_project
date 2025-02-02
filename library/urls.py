"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

import catalog.views
import blog.views
import personal.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', catalog.views.main),
    path('catalog/', include('catalog.urls')),
    path('blog/', include('blog.urls')),
    path('personal/', include('personal.urls')),
    re_path(r'^catalog/genre/\w+/book-search/\S*', catalog.views.search_book_by_genre),
    re_path(r'^catalog/book-search/\S*', catalog.views.search_book),
    re_path(r'^catalog/', catalog.views.redirect),
    re_path(r'^blog/', blog.views.redirect),
    re_path(r'^personal/', personal.views.redirect),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
