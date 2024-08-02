from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

#configuracion de SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/repaso_flask_primer_semestre"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Marca, Pais, Caracteristica, Stock, Accesorio, Persona, Fabricante, Equipo, Modelo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/equipos_list', methods=["POST","GET"])
def equipos():
    equipos = Equipo.query.all()
    return render_template('equipos_list.html')

@app.route('/accesorio_list')
def accesorios():
    return render_template('accesorio_list.html')

@app.route('/caracteristica_list')
def caracteristicas():
    return render_template('caracteristica_list.html')

@app.route('/fabricante_list', methods=['POST', 'GET'])
def fabricantes():
    fabricantes = Fabricante.query.all()
    paises = Pais.query.all()
    if request.method == 'POST':
        fabricante_nombre = request.form['nombre']
        pais_id = request.form['pais']
        nuevo_fabricante = Fabricante(nombre=fabricante_nombre, pais_id=pais_id)
        db.session.add(nuevo_fabricante)
        db.session.commit()
        return redirect(url_for('fabricantes'))
    return render_template('fabricante_list.html', fabricantes=fabricantes, paises=paises)

@app.route('/marca_list', methods=["POST","GET"])
def marcas():
    marcas = Marca.query.all()
    fabricantes = Fabricante.query.all()
    if request.method=="POST":
        nombre = request.form["nombre"]
        nueva_marca = Marca(nombre=nombre)
        db.session.add(nueva_marca)
        db.session.commit()
        return redirect(url_for("marcas"))
    return render_template('marca_list.html', marcas = marcas, fabricantes = fabricantes)

@app.route('/modelo_list', methods=["POST","GET"])
def modelos():
    modelos = Modelo.query.all()
    marcas = Marca.query.all()
    if request.method=="POST":
        nombre = request.form["nombre"]
        anio = request.form["anio_fabricacion"]
        modelo_nuevo = Modelo(
            nombre = nombre,
            anio_fabricacion = anio,
        )
        db.session.add(modelo_nuevo)
        db.session.commit()
        return redirect (url_for("modelos"))
    return render_template('modelo_list.html', modelos = modelos, modelo_nuevo = modelo_nuevo, marcas = marcas)
        

@app.route('/proveedor_list')
def proveedores():
    return render_template('proveedor_list.html')

@app.route('/stock', methods=['GET', 'POST'])
def stock():
    equipos = Equipo.query.all()
    stocks = Stock.query.all()
    if request.method == 'POST':
        equipo_id = request.form['equipo_id']
        cantidad_disponible = request.form['cantidad_disponible']
        cantidad_minima = request.form['cantidad_minima']
        ubicacion_almacen = request.form['ubicacion_almacen']
        nuevo_stock = Stock(cantidad_disponible=cantidad_disponible, cantidad_minima=cantidad_minima, ubicacion_almacen=ubicacion_almacen)
        db.session.add(nuevo_stock)
        db.session.commit()
        return redirect(url_for('stock'))
    return render_template('stock.html', stocks=stocks, equipos=equipos)

