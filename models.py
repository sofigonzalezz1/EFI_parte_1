from app import db

""" class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def _str_(self):
        return self.nombre
    
class Tipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def _str_(self):
        return self.nombre """

""" class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelo_id'), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    costo = db.Column(db.Integer, nullable=False) """

""" class Modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    fabricante_id = db.Column(db.Integer, db.ForeignKey('fabricante_id'), nullable=False) """

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(50), nullable=False)

class Pais(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    fabricantes = db.relationship('Fabricante', backref=db.backref('pais'), lazy=True)

class Fabricante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    pais_id = db.Column(db.Integer, db.ForeignKey('pais_id'), nullable=False)
 
class Caracteristica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    caracteristicas = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(150), nullable=False)

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cantidad_disponible = db.Column(db.Integer, nullable=False)
    cantidad_minima = db.Column(db.Integer, nullable=False)
    ubicacion_almacen = db.Column(db.String(100), nullable=False)

""" class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    persona_id = db.Column(db.Integer, db.ForeignKey('persona_id'), nullable=False)
    contacto = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False) """
    
class Accesorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    accesorio = db.Column(db.String(100), nullable=False)
    compatibilidad = db.Column(db.Boolean)

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    documento = db.Column(db.String(20), nullable=False)
    genero = db.Column(db.String(10), nullable=False)






    
