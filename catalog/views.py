from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from catalog.books import Book, BookBuilder
from database import DBConnect, PGBooksManager



# Create your views here.
def main(request: HttpRequest):

    book1 = Book("Совершенные. Тайны Пантеона",
                 'Приключения',
                "«Если Август Рэй Эттвуд пройдет свой темный путь, он превзойдет дьявола и наш мир падет…»",
                107)

    book2 = Book("Железное пламя",
                 'Фантастика',
                 "Никто не ожидал, что Вайолет Сорренгейл выживет в Военной академии Басгиат, включая саму Вайолет. ",
                 25)

    book3 = Book("Зеленый свет",
                 'Биография',
                 "Впервые на русском – одно из главных книжных событий 2020 года, «Зеленый свет» знаменитого Мэттью Макконахи (лауреат «Оскара» за главную мужскую роль в фильме «Далласский клуб покупателей»",
                 78)

    data = list()
    data.append(book1)
    data.append(book2)
    data.append(book3)

    context = {
        "data": data,
        "count": len(data),
    }

    return render(request, template_name='books.html', context=context)


def get_by_genre(request: HttpRequest, genre=None):
    # Получить список категорий из таблицы Categories
    genre_data = ['classic', 'adventure', 'fantastic']

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

        # Запрос к БД по 2 параметрам и получение данных в data
        # Посмотреть что пришли непустые данные
        # Либо допустим пришли следующие 2 книги book1 и book2
        book1 = Book("Совершенные. Тайны Пантеона",
                     "фантастика",
                     "«Если Август Рэй Эттвуд пройдет свой темный путь, он превзойдет дьявола и наш мир падет…»",
                     107)

        book2 = Book("Железное пламя",
                     "фантастика",
                     "Никто не ожидал, что Вайолет Сорренгейл выживет в Военной академии Басгиат, включая саму Вайолет. ",
                     25)

        book3 = Book("Зеленый свет",
                     "биография",
                     "Впервые на русском – одно из главных книжных событий 2020 года, «Зеленый свет» "
                     "знаменитого Мэттью Макконахи (лауреат «Оскара» за главную мужскую роль в фильме "
                     "«Далласский клуб покупателей»",
                     78)

        data = list()
        data.append(book1)
        data.append(book2)
        data.append(book3)

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

            context = {
                "data": data,
                'count': len(data),
            }

        return render(request,
                      template_name='books.html',
                      context=context)


def redirect(request: HttpRequest):
    return render(request, '404.html')

