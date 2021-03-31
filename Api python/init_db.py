#Se crea la base de datos

import sqlite3

#Se abre una conexión con el archivo de la base de datos
connection = sqlite3.connect('database.db')

#Se abre el archivo y se ejecuta su contenido
with open('schema.sql') as f:
    connection.executescript(f.read())

#Se crea un objeto cursor
cur = connection.cursor()

#Se crean 2 entradas de blog en la tabla
cur.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
            ('First Post', 'Content for the first post'))

cur.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
            ('Second Post', 'Content for the second post'))

connection.commit()
connection.close()