from abc import ABC, abstractmethod
from .books import Book, BooksContainer
import psycopg2


class DBConnect:

    _instance = None

    @classmethod
    def get_connect(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = psycopg2.connect(*args, **kwargs)
        return cls._instance


class DBManager(ABC):

    @staticmethod
    @abstractmethod
    def create(connect, book: Book):
        ...

    @staticmethod
    @abstractmethod
    def read(connect, book: Book):
        ...

    @staticmethod
    @abstractmethod
    def update(connect, old_book: Book, new_book: Book):
        ...

    @staticmethod
    @abstractmethod
    def delete(connect, book: Book):
        ...


class PGBooksManager(DBManager):

    @staticmethod
    def create(connect, book: Book):
        # Вызвать запрос вставки данных из объекта в таблицу
        ...

    @staticmethod
    def read(connect, book: Book) -> list[Book]:

        try:
            with connect.cursor() as cursor:

                params = (book.title, )
                query = """SELECT * 
                           FROM books
                           WHERE title = %s"""
                cursor.execute(query, params)
                data = cursor.fetchall()

                if data:
                    container = BooksContainer()
                    container.create_list_books(data)
                    return container.get_list_books()
                else:
                    raise Exception(f"Не найдена запись с параметрами {params}")
        except (Exception, psycopg2.Error) as e:
            print(e)

    @staticmethod
    def update(connect, index_old_book: int, new_book: Book):
        # Обновить данные о книге в таблице
        ...

    @staticmethod
    def delete(connect, book: Book):
        # Удалить девайс
        ...

