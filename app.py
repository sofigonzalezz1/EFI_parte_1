from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

#configuracion de SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/repaso_flask_primer_semestre"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Marca, Pais, Caracteristica, Stock, Accesorio, Persona, Fabricante

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/equipos_list')
def equipos():
    return render_template('equipos_list.html')

@app.route('/accesorio_list')
def accesorios():
    return render_template('accesorio_list.html')

@app.route('/caracteristica_list')
def caracteristicas():
    return render_template('caracteristica_list.html')

@app.route('/fabricante_list')
def fabricantes():
    return render_template('fabricante_list.html')

@app.route('/marca_list')
def marcas():
    return render_template('marca_list.html')

@app.route('/modelo_list')
def modelos():
    return render_template('modelo_list.html')

@app.route('/proveedor_list')
def proveedores():
    return render_template('proveedor_list.html')

@app.route('/stock')
def stock():
    return render_template('stock.html')

