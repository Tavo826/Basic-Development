import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

#request    -> para acceder a los datos de solicitud entrantes que se enviarán a través del HTML
#url_for()  -> para generar URLs
#flash()    -> para mostrar un mensaje cuando se procesa una solicitud
#redirect() -> redirige al cliente a una ubicación diferente

app = Flask(__name__)
#Protege las sesiones para luego almacenar los mensajes en el navegador del cliente
app.config['SECRET KEY'] = 'your secret key'

#El usuario puede| acceder a la información almacenada en la sesión
#pero no puede modificarla si no tiene la clave secreta

#Función que crea una conexión con la base de datos
def get_db_connection():
    #Se abre una conexión con el archivo
    conn = sqlite3.connect('database.db')
    #Se establece un atributo
    #Row para poder tener acceso a las columnas basado en nombre
    #esto devuelve filas que se comportan como diccionarios
    conn.row_factory = sqlite3.Row
    return conn

#Se necesita obtener la entrada de blog por su ID en la base de datos
def get_post(post_id):
    #Se abre una conexión de base de datos
    conn = get_db_connection()
    #Se ejecuta una consulta para seleccionar todas las entradas de la tabla
    #post_id determina la entrada de blog recuperar
    #El método fetchone() para obtener el resultado y almacenarlo en post
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    #Se cierra la conexión con la base de datos
    conn.close()
    #Si la variable es None es porque no hay resultados en la base de datos
    if post is None:
        #Se termina la ejecución con un código de error
        abort(404)
    return post

@app.route('/')
def index():
    #Se abre una conexión de base de datos
    conn = get_db_connection()
    #Se ejecuta una consulta para seleccionar todas las entradas de la tabla
    #se implementa fetchall() para recuperar todas las filas del resultado de la consulta
    #devolviendo una lista de las entradas insertadas en la base de datos
    posts = conn.execute('SELECT * FROM posts').fetchall()
    #Se cierra la conexión con la base de datos
    conn.close()
    #El argumento posts permite acceder a las entradas del blog en la plantilla index.html
    return render_template('index.html', posts=posts)

#Se añade una regla variable para especificar que la parte tras / es un entero positivo
@app.route('/<int:post_id>')
#Se obtiene la entrada de blog asociada al ID y se almacena el resultado en post
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

#Se muestra un formulario que se debe completar para crear una nueva entrada de blog
@app.route('/create', methods=('GET', 'POST'))
def create():
    #Recibe una solicitud POST
    #Comprobando la solicitud
    if request.method == 'POST':
        #Se extrae la información de la publicación
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            #Se conecta con la base de datos
            conn = get_db_connection()
            #Se publican los datos ingresados
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                        (title, content))
                    
            conn.commit()
            conn.close()
            #Redirige al cliente a la página de índice
            return redirect(url_for('index'))

    return render_template('create.html')

#Editando una entrada
@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    #Recupera la entrada asociada al ID
    post = get_post(id)

    if request.method == 'POST':
        #Se extraen los datos
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            #Actualiza la tabla posts
            conn.execute('UPDATE post SET title = ?, content = ?'
                        'WHERE id = ?',
                        (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('edit.html', post=post)

#Eliminar una entrada
@app.route('/<int:id>/delete', methods=('POST', 'GET'))
def delete(id):
    #Se obtiene la entrada de la base de datos
    post = get_post(id)
    #Se abre la conexión con la base de datos
    conn = get_db_connection()
    #Se elimina la entrada
    conn.execute('DELETE FROM post WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was succefuly deleted!'.format(post['title']))
    #Redirige a la página de índice
    return redirect(url_for('index'))

app.run()