/*Se elimina cualquier tabla llamada posts*/
DROP TABLE IF EXISTS posts;

/*Se crea la tabla*/
CREATE TABLE posts(
    /*Entero que representa una clave primaria, para cada entrada del blog*/
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    /*NOT NULL, la columna no debería estar vacía
    CURRENT_TIMESTAMP es la hora en la que se añade la entrada*/
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAP,
    /*Título de la entrada*/
    title TEXT NOT NULL,
    /*contenido de la entrada*/
    content TEXT NOT NULL
);