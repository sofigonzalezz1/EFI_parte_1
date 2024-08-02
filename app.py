from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

#configuracion de SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/repaso_flask_primer_semestre"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import db, Marca, Pais, Caracteristica, Stock, Accesorio, Persona, Fabricante, Equipo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/equipos_list')
def equipos():
    return render_template('equipos_list.html')

@app.route('/accesorio_list', methods=['POST', 'GET'])
def accesorios():
    accesorios = Accesorio.query.all()
    compatible=True
    if request.method == 'POST':
        for accesorio in accesorios:
            if not accesorio.compatibilidad:
                compatible = False
    return render_template('accesorio_list.html', accesorio=accesorios, compatible=compatible)

@app.route('/caracteristica_list', methods=['POST', 'GET'])
def caracteristicas():
    caracteristicas = Caracteristica.query.all()
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

@app.route('/marca_list')
def marcas():
    return render_template('marca_list.html')

@app.route('/modelo_list')
def modelos():
    return render_template('modelo_list.html')

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

