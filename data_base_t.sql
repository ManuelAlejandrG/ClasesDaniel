mysql -u root -p

SELECT * FROM autores;

SELECT * FROM libros;

SELECT nombre, apellido FROM autores;

SELECT DISTINCT titulo FROM libros;

SELECT COUNT(titulo) FROM libros;

SELECT titulo FROM libros WHERE autor_id=1;

SELECT titulo FROM libros WHERE autor_id <>1;

SELECT fecha_publicacion FROM libros WHERE fecha_publicacion<"2000" and fecha_publicacion>"1937";

SELECT fecha_publicacion FROM libros WHERE fecha_publicacion BETWEEN "1937-01-01" and "2000-01-01";

SELECT fecha_publicacion FROM autores WHERE pais_origen IN ('USA','España');

SELECT titulo, autor_id FROM libros ORDER BY titulo;

SELECT nombre, apellido FROM autores ORDER BY apellido DESC;
