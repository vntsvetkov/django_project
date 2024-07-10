
CREATE TABLE IF NOT EXISTS genres (
	genre_id SERIAL PRIMARY KEY,
	name_genre VARCHAR(50) NOT NULL UNIQUE
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
('Классика'),
('Приключения'),
('Фантастика');

INSERT INTO books(title, genre_id, description, count_load)
VALUES
('Совершенные. Тайны Пантеона', 3, 'Если Август Рэй Эттвуд пройдет свой темный путь, он превзойдет дьявола и наш мир падет', 0);


