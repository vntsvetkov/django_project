from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from catalog.books import Book, BookBuilder, BooksContainer
from catalog.database import DBConnect, PGBooksManager


# Create your views here.
def main(request: HttpRequest):
    connect = DBConnect.get_connect(dbname='library',
                                    host='localhost',
                                    port=5432,
                                    user='postgres',
                                    password='postgres')

    cursor = connect.cursor()
    query = """ SELECT * FROM books """
    cursor.execute(query)
    container = BooksContainer()
    container.create_list_books(cursor.fetchall())
    data = container.get_list_books()
    count = len(data) if data is not None else 0
    cursor.close()

    cursor = connect.cursor()
    query = """ SELECT name_genre, translation FROM genres """
    cursor.execute(query)
    genres = {item[0]: "http://127.0.0.1:8000/catalog/genre/" + item[1] + '/' for item in cursor.fetchall()}
    print(genres)
    cursor.close()

    connect.close()

    context = {
        "data": data,
        "count": count,
        "genres": genres,
    }

    return render(request, template_name='books.html', context=context)


def get_by_genre(request: HttpRequest, genre=None):
    # connect = DBConnect.get_connect(dbname='library',
    #                                 host='localhost',
    #                                 port=5432,
    #                                 user='postgres',
    #                                 password='postgres')
    #
    # cursor = connect.cursor()
    # query = """ SELECT translation FROM genres """
    # cursor.execute(query)
    # data = cursor.fetchall()
    # genre_data = [item[0] for item in data]

    genre_data = ['classic']
    if genre in genre_data:
        title = None
        author = None
        if request.method == "GET":
            title = request.GET.get('title', '')
            author = request.GET.get('author', '')

        elif request.method == "POST":
            title = request.POST.get('title', '')
            author = request.POST.get('author', '')

        if not title and not author:
            return HttpResponseNotFound(f""" <h1> В жанре {genre} этой книги не найдено </h1>""")

        data = list()
        context = {
            "data": data
        }

        return render(request, template_name='books.html', context=context)

    else:
        return HttpResponseNotFound(f""" <h1> В жанре {genre} книг не найдено </h1>""")


def search_book(request):
    if request.method == "GET":
        title = request.GET.get('title', '')

        if not title:
            context = {
                'count': 0
            }
        else:
            connect = DBConnect.get_connect(dbname='library',
                                            host='localhost',
                                            port=5432,
                                            user='postgres',
                                            password='postgres')

            builder = BookBuilder()
            builder.create()
            builder.set_title(title)
            book = builder.get_book()
            data = PGBooksManager.read(connect, book)
            count = len(data) if data is not None else 0
            context = {
                "data": data,
                'count': count,
            }

        return render(request,
                      template_name='books.html',
                      context=context)


def redirect(request: HttpRequest):
    return render(request, '404.html')

