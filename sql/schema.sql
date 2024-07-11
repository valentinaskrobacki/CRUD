USE crud_peliculas;

CREATE TABLE IF NOT EXISTS movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    director VARCHAR(100),
    anio INT,
    portada VARCHAR(255),
    sinopsis TEXT
);

INSERT INTO movies (titulo, director, anio, portada, sinopsis)
VALUES 
    ('Titanic', 'James Cameron', 1997, 'https://example.com/titanic.jpg', 'Una historia de amor en el trágico hundimiento del Titanic.'),
    ('The Shawshank Redemption', 'Frank Darabont', 1994, 'https://example.com/shawshank.jpg', 'La historia de un hombre inocente encarcelado que mantiene la esperanza.'),
    ('The Godfather', 'Francis Ford Coppola', 1972, 'https://example.com/godfather.jpg', 'La historia de una poderosa familia de la mafia en Nueva York.'),
    ('Pulp Fiction', 'Quentin Tarantino', 1994, 'https://example.com/pulpfiction.jpg', 'Una serie de historias entrelazadas sobre criminales en Los Ángeles.'),
    ('The Dark Knight', 'Christopher Nolan', 2008, 'https://example.com/darkknight.jpg', 'Batman se enfrenta al Joker en una batalla por Gotham City.'),
    ('Forrest Gump', 'Robert Zemeckis', 1994, 'https://example.com/forrestgump.jpg', 'La vida de Forrest Gump, un hombre con un coeficiente intelectual bajo pero buen corazón.'),
    ('Fight Club', 'David Fincher', 1999, 'https://example.com/fightclub.jpg', 'Un hombre desilusionado forma un club de pelea clandestino que evoluciona en algo mucho más.'),
    ('Inception', 'Christopher Nolan', 2010, 'https://example.com/inception.jpg', 'Un ladrón experimenta con el robo de información del subconsciente durante los sueños.'),
    ('The Matrix', 'Lana Wachowski, Lilly Wachowski', 1999, 'https://example.com/matrix.jpg', 'Un hacker descubre que la realidad es una simulación controlada por máquinas.'),
    ('The Lord of the Rings: The Fellowship of the Ring', 'Peter Jackson', 2001, 'https://example.com/lotr.jpg', 'Frodo emprende un viaje para destruir un anillo mágico y salvar a la Tierra Media.'),
    ('Goodfellas', 'Martin Scorsese', 1990, 'https://example.com/goodfellas.jpg', 'La vida de un hombre joven que se une a la mafia y su ascenso dentro de la organización.'),
    ('Schindlers List', 'Steven Spielberg', 1993, 'https://example.com/schindlerslist.jpg', 'La historia real de Oskar Schindler, un empresario alemán que salva a judíos durante el Holocausto.'),
    ('The Silence of the Lambs', 'Jonathan Demme', 1991, 'https://example.com/silenceofthelambs.jpg', 'Un agente del FBI busca la ayuda de Hannibal Lecter, un psicópata encarcelado, para atrapar a otro asesino en serie.'),
    ('The Departed', 'Martin Scorsese', 2006, 'https://example.com/departed.jpg', 'Un policía se infiltra en la mafia mientras un mafioso se infiltra en la policía en Boston.'),
    ('Gladiator', 'Ridley Scott', 2000, 'https://example.com/gladiator.jpg', 'Un general romano es traicionado y busca venganza como gladiador en el Coliseo.');
