CREATE DATABASE IF NOT EXISTS library;

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
	description TEXT NOT NULL DEFAULT 'Без описания',
	count_load INTEGER NOT NULL DEFAULT 0,
	FOREIGN KEY(genre_id)
        REFERENCES genres(genre_id)
            ON DELETE NO ACTION
);


INSERT INTO genres(name_genre)
VALUES
('Биография', 'biography'),
('Классика', 'classic'),
('Приключения', 'adventures'),
('Фантастика', 'fantastic');

INSERT INTO books(title, genre_id, description, count_load)
VALUES
('Тайны Пантеона', 4, 'Если Август Рэй Эттвуд пройдет свой темный путь, он превзойдет дьявола и наш мир падет', 0),
('Железное пламя', 4, 'Никто не ожидал, что Вайолет Сорренгейл выживет в Военной академии Басгиат, включая саму Вайолет.', 0),
('Зеленый свет', 1, '«Зеленый свет» знаменитого Мэттью Макконахи (лауреат «Оскара» за главную мужскую роль в фильме «Далласский клуб покупателей', 0);


