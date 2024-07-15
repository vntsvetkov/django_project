from abc import ABC, abstractmethod


class Book:

    def __init__(self):

        self.title = None
        self.genre = None
        self.author = None
        self.description = None
        self.rating = None
        self.count_load = None
        self.cover = None


class Builder(ABC):

    @abstractmethod
    def create(self):
        ...

    @abstractmethod
    def set_title(self, title):
        ...

    @abstractmethod
    def set_genre(self, genre):
        ...

    @abstractmethod
    def set_author(self, author):
        ...

    @abstractmethod
    def set_description(self, description):
        ...

    @abstractmethod
    def set_rating(self, rating):
        ...

    @abstractmethod
    def set_count_load(self, count_load):
        ...

    @abstractmethod
    def set_cover(self, cover):
        ...

    @abstractmethod
    def get_book(self):
        ...


class BookBuilder(Builder):

    _book: Book

    def create(self):
        self._book = Book()

    def set_title(self, title):
        self._book.title = title

    def set_genre(self, genre):
        self._book.genre = genre

    def set_author(self, author):
        self._book.author = author

    def set_description(self, description):
        self._book.description = description

    def set_rating(self, rating):
        self._book.rating = rating

    def set_count_load(self, count_load):
        self._book.count_load = count_load

    def set_cover(self, cover):
        self._book.cover = cover

    def get_book(self):
        return self._book


class BookCreator:

    def __init__(self, builder: Builder):
        self._builder = builder

    def change_builder(self, builder: Builder):
        self._builder = builder

    def make(self, book: tuple) -> Book:
        self._builder.create()
        self._builder.set_title(book[1])
        self._builder.set_genre(book[2])
        self._builder.set_author(book[3])
        self._builder.set_description(book[4])
        self._builder.set_rating(book[5])
        self._builder.set_count_load(book[6])
        img_path = '../static/img/covers/' + str(book[7]) + '.jpg'
        self._builder.set_cover(img_path)
        return self._builder.get_book()


class BooksContainer:

    def __init__(self):
        self._books: list[Book] = []

    def create_list_books(self, data: list) -> None:
        builder = BookBuilder()
        creator = BookCreator(builder)

        for record in data:
            book = creator.make(record)
            self._books.append(book)

    def add_book(self, book: Book):
        self._books.append(book)

    def get_list_books(self):
        return self._books
