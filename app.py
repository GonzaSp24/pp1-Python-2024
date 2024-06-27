#import requests

#from flask import (Flask,
#                jsonify, 
#                render_template,
#                request
#                )

#app = Flask(__name__)

from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/explicacion_db' #conexion a la base de datos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Marca, Tipo, Vehiculo


#listado_nombres = ['Juan', 'Pepe', 'Pedro']

# listado_personas = [
#     dict(
#         name = dict(
#         first = "Juan Pablo" ,
#         last ="Vanci"
#     ),
#     location = dict(
#         city = "Buenos Aires",
#     ),
#     email = "jpv@gmail.com"
#     ),
#     dict(
#         name = dict(
#         first = "Gonza" ,
#         last ="Franc"
#     ),
#     location = dict(
#         city = "Paris",
#     ),
#     email = "gs2@gmail.com"
#     ),
#     ]

# #diccionario_nombres = [
# #    dict(
# #        nombre = 'Ana',
# #        edad = 30,
# #        pais= 'Argentina',
# #        
# #    ),
# #    dict(
# #        nombre = 'Pepe',
# #        edad =28,
# #        pais= 'Peru',
# #        
# #    ),
# #    dict(
# #        nombre = 'Jose',
# #        edad = 25,
# #        pais= 'Bolivia',
# #        
# #    ),
# #]

# @app.route('/')
# def home(): 
#     return render_template('index.html')
# # @app.route('/acerca_de')
# # def about():
# #     return "<h3>'Soy un pagina de acerca de'</h3> <a href='/'>Volver</a>"

# # @app.route("/bienvenido/<nombre>")
# # def welcome(nombre):
# #     return f"Bienvenido {nombre}"

# # @app.route("/suma/<int:num1>/<int:num2>")
# # def suma(num1, num2):
# #     return f"La suma de {num1} y {num2} es {num1 + num2}"
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/bandas')
# def bandas():
#     return render_template('bandas.html')

# @app.route('/exponentes')
# def exponentes():
#     return render_template('exponentes.html')

# @app.route ('/personas')
# def personas():
#     return render_template(
#         'personas.html'
#     )
#     from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/') # app es la instancia, route el metodo, '/' es el disparador
# def index():
#     return render_template(
#         'index.html',
#     )

# @app.route('/info') # app es la instancia, route el metodo, '/' es el disparador
# def informacion():
#     return render_template(
#         'informacion.html',
#     )

# @app.route('/bienvenido/<nombre>')
# def bienvenida(nombre):
#     return render_template(
#         'bienvenida.html',app.py
#     )
#  #@app.route ('/personas')
#  #def personas():
#    #      return render_template(
#      #        'personas.html',
#        #      nombres = listado_nombres,
#          #    diccionario_personas= diccionario_nombres,
#            #  
#          #)

# @app.route('/personas')
# def personas():
#     #peticion= requests.getuenos Aires"(url= "https://randomuser.me/api/?results=20")
#     #respuesta = peticion.json()
#     #lista_personas = respuesta['results'] #respuesta.GET.('results')
#     listado = listado_personas
#     return render_template(
#         'personas.html',
#     #    listado =lista_personas
#         listado = listado
#     )
    
# @app.route('/personas_add', methods = ['POST', 'GET'])# Si explicito un metodo tengo que explicitar todos
# def agregar_personas():
#     if request.method == 'POST':
#         first_name =request.form ['name']
#         apellido = request.form ['lastname']
#         email = request.form ['email']
#         ciudad = request.form ['city']   
        
#         persona = dict(
#             name = dict(
#                 first = first_name ,
#                 last = apellido   
#         ),
#         location = dict(
#             city = ciudad,
#         ),
#         email = email
#         )
#         #print(first_name,apellido, email, ciudad)
#         listado_personas.append(persona)
#     return render_template (
#         'add_personas.html',                    
#                             )