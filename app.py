from flask import Flask, render_template, url_for, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

#configuracion de SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/repaso_flask_primer_semestre"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)



from models import Marca, Pais, Caracteristica, Stock, Accesorio, Persona, Fabricante, Equipo, Modelo, Proveedor


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/equipos_list', methods=["POST","GET"])
def equipos():
    equipos = Equipo.query.all()
    return render_template('equipos_list.html')

@app.route('/accesorio_list', methods=['POST', 'GET'])
def accesorios():
    equipos = Equipo.query.all()
    accesorios = Accesorio.query.all()

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        compatibilidad = request.form.get('compatibilidad') == 'true'
        equipo_id = request.form.get('Equipos')

        nuevo_accesorio = Accesorio(
            accesorio=nombre,
            compatibilidad=compatibilidad,
            equipo_id=equipo_id
        )
        db.session.add(nuevo_accesorio)
        db.session.commit()

        return redirect(url_for('accesorios'))

    return render_template('accesorio_list.html', accesorios=accesorios, equipos=equipos)

@app.route('/caracteristica_list', methods=['POST', 'GET'])
def caracteristicas():
    equipos = Equipo.query.all()
    caracteristicas = []
    selected_equipo_id = None

    if request.method == 'POST':
        selected_equipo_id = request.form.get('equipo_id')
        caracteristicas = Caracteristica.query.filter_by(equipo_id=selected_equipo_id).all()
        
        if 'agregar_caracteristica' in request.form:
            nueva_caracteristica = request.form.get('nueva_caracteristica')
            descripcion = request.form.get('descripcion')
            nueva_caracteristica_entry = Caracteristica(
                equipo_id=selected_equipo_id,
                caracteristicas=nueva_caracteristica,
                descripcion=descripcion
            )
            db.session.add(nueva_caracteristica_entry)
            db.session.commit()
            caracteristicas = Caracteristica.query.filter_by(equipo_id=selected_equipo_id).all()

    return render_template('caracteristica_list.html', equipos=equipos, caracteristicas=caracteristicas, selected_equipo_id=selected_equipo_id)

@app.route('/fabricante_list', methods=['POST', 'GET'])
def fabricantes():
    fabricantes = Fabricante.query.all()
    paises = Pais.query.all()
    if request.method == 'POST':
        fabricante_nombre = request.form['nombre']
        pais_id = request.form['pais']
        if not fabricante_nombre or not pais_id:
            return "Datos incompletos", 400
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
        categoria = request.form["categoria"]
        fabricante_id = request.form["fabricante_id"]
        if not nombre or not categoria or not fabricante_id:
            return "Datos incompletos", 400
        
        try:
            fabricante_id = int(fabricante_id)  # Asegurarse de que el ID del fabricante es un entero
            nueva_marca = Marca(nombre=nombre, categoria=categoria, fabricante_id=fabricante_id)
            db.session.add(nueva_marca)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return str(e), 500
        return redirect(url_for("marcas"))
    return render_template('marca_list.html', marcas = marcas, fabricantes = fabricantes)

@app.route('/modelo_list', methods=["POST","GET"])
def modelos():
    modelos = Modelo.query.all()
    marcas = Marca.query.all()
    if request.method=="POST":
        nombre = request.form["nombre"]
        marca_id = request.form["marca_id"]

        print(f"Datos recibidos: nombre={nombre}, marca_id={marca_id}")

        if not nombre or not marca_id:
            return "Datos incompletos", 400
        try:
            marca_id = int(marca_id)
            marca = Marca.query.get(marca_id)
            if not marca:
                return "Marca no existe", 400
            
            modelo_nuevo = Modelo(
                nombre=nombre,
                marca_id=marca_id
            )
            db.session.add(modelo_nuevo)
            db.session.commit()
            return redirect(url_for("modelos"))

        except Exception as e:
            db.session.rollback()
            return f"Error al crear el modelo: {str(e)}", 400
    
    return render_template('modelo_list.html', modelos=modelos, marcas=marcas)
        

@app.route('/proveedor_list', methods=["POST","GET"])
def proveedor_list():
    if request.method == 'POST':
        if 'agregar' in request.form:
            nueva_razon_social = request.form['razon_social']
            nuevo_telefono = request.form['telefono']
            nuevo_mail = request.form['mail']
            nuevo_cuit = request.form['cuit']
            nuevo_proveedor = Proveedor(
                razon_social=nueva_razon_social,
                telefono=nuevo_telefono,
                mail=nuevo_mail,
                cuit=nuevo_cuit,
            )
            db.session.add(nuevo_proveedor)
            db.session.commit()
            flash('Proveedor agregado exitosamente.')

        # Acción de editar
        elif 'editar' in request.form:
            proveedor_id = request.form['proveedor_id']
            proveedor = Proveedor.query.get(proveedor_id)
            proveedor.razon_social = request.form['razon_social']
            proveedor.telefono = request.form['telefono']
            proveedor.mail = request.form['mail']
            proveedor.cuit = request.form['cuit']
            db.session.commit()
            flash('Proveedor actualizado exitosamente.')

        # Acción de eliminar
        elif 'eliminar' in request.form:
            proveedor_id = request.form['proveedor_id']
            proveedor = Proveedor.query.get(proveedor_id)
            db.session.delete(proveedor)
            db.session.commit()
            flash('Proveedor eliminado exitosamente.')

        return redirect(url_for('proveedores_list'))

    # Acción de ver (GET request)
    proveedores = Proveedor.query.all()
    return render_template('proveedor_list.html', proveedores=proveedores)


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

