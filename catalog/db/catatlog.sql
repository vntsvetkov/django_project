CREATE DATABASE library
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LOCALE_PROVIDER = 'libc'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

DROP TABLE IF EXISTS genres;
DROP TABLE IF EXISTS books;

CREATE TABLE IF NOT EXISTS genres (
	genre_id SERIAL PRIMARY KEY,
	name_genre VARCHAR(50) NOT NULL UNIQUE,
	translation VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS books (
	book_id SERIAL PRIMARY KEY,
	title TEXT NOT NULL CHECK(LENGTH(title) > 0),
	genre_id INTEGER NOT NULL,
	author VARCHAR(30) NOT NULL CHECK(LENGTH(author) > 0) DEFAULT 'Неизвестно',
	description TEXT NOT NULL DEFAULT 'Без описания',
	rating NUMERIC(3,2) NOT NULL CHECK(rating BETWEEN 0 and 5) DEFAULT 0,
	count_load INTEGER NOT NULL DEFAULT 0,
	cover INTEGER NOT NULL DEFAULT 0,
	FOREIGN KEY(genre_id)
        REFERENCES genres(genre_id)
            ON DELETE NO ACTION
);


INSERT INTO genres(name_genre, translation)
VALUES
('Биография', 'biography'),
('Классика', 'classic'),
('Приключения', 'adventures'),
('Фантастика', 'fantastic');

INSERT INTO books(title, genre_id, author, description, rating, count_load)
VALUES
('Тайны Пантеона', 4, 'Марина Суржевская', 'Если Август Рэй Эттвуд пройдет свой темный путь, он превзойдет дьявола и наш мир падет', 4.9, 0),
('Железное пламя', 4, 'Ребекка Яррос', 'Никто не ожидал, что Вайолет Сорренгейл выживет в Военной академии Басгиат, включая саму Вайолет.', 4.7, 0),
('Зеленый свет', 1, 'Мэттью Макконахи', '«Зеленый свет» знаменитого Мэттью Макконахи (лауреат «Оскара» за главную мужскую роль в фильме «Далласский клуб покупателей', 4, 0);

