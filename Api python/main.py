from flask import Flask

# Flask es un gestor de rutas
# WSGI -> Web Service Gateway Interface

#Se crea el objeto API
app = Flask(__name__)

#Dónde se va a correr la API
app.run(debug = True)