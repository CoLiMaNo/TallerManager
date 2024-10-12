# Gracias a estas líneas de código, enfrento el mundo cada día 💪
#  Todas las clases van aqui:

from sqlalchemy import *
from sqlalchemy.orm import *
from datetime import datetime
import db # conecta el fichero db.py con models.py



class Cliente(db.Base_mobile):

    '''Clase Cliente
    incluye id_cliente, fecha_alta, nombre, telefono, direccion y correo

    args
    -id_cliente: es un numero integer que compone el codigo del cliente
    -fecha_alta: es un registro unico por cliente que hace referencia a la fecha del registro de alta
    -nombre: es un string que compone el nombre del cliente
    -telefono: es un String que compone el numero de telefono del cliente
    -direccion: es un string que compone la direccion del cliente
    -correo: es un string que compone la direccion email del cliente
    '''

    __tablename__ = 'clientes' # nombre de la tabla
    __table_args__ = {'sqlite_autoincrement': True}  # (esto fuerza un valor autoincrementado como el id) diccionario de diferentes claves:valores (configuracion  de la tabla)

    # Estructura de la tabla clientes
    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    fecha_alta = Column(DateTime, default=datetime.utcnow)
    nombre = Column(String(255), nullable=False)
    telefono = Column(String, nullable=False)
    direccion = Column(String(255), nullable=False)
    correo = Column(String(255), nullable=False)

    # Relacion uno a muchos
    vehiculos = relationship('Vehiculo', back_populates ='clientes')
    ingresos = relationship('Ingreso', back_populates = 'clientes')
    #registros = relationship('Registro', back_populates ='clientes')

    # Costructor de la clase Cliente
    def __init__(self, fecha_alta, nombre, telefono, direccion, correo):
        '''costructor de la clase Cliente'''
        self.fecha_alta = fecha_alta # Fecha de registro del cliente
        self.nombre = nombre  # Nombre del cliente
        self.telefono = telefono # Telefono de contacto del cliente
        self.direccion = direccion  # direccion del cliente
        self.correo = correo  # email del cliente

        print('Cliente creado con exito')

    # metodo STR nos muestra la informacion
    def __str__(self):
        return "ID: {}, {}, Direccion: {} ".format(self.id_cliente, self.nombre, self.direccion, self.correo)


class Vehiculo(db.Base_mobile):
    '''Clase Vehiculo
    incluye id_vehiculo, marca, modelo, matricula, kilometros

    args
    -id_vehiculo: es un numero integer que compone el codigo del vehiculo
    -marca: es un string que compone la marce del vehiculo
    -modelo: es un string que compone el modelo del vehiculo
    -matricula: es un string que compone la matricula del vehiculo
    -kilometros: es un string que compone los kilometros desde el primer ingreso o alta en la DB
    '''

    __tablename__ = 'vehiculos'
    __table_args__ = {'sqlite_autoincrement': True}

    # Estructura de la tabla vehiculos
    id_vehiculo = Column(Integer, primary_key=True, autoincrement=True)
    fecha_alta = Column(DateTime, default=datetime.utcnow)
    marca = Column(String(255), nullable=False)
    modelo = Column(String(255), nullable=False)
    matricula = Column(String(255), nullable=False)
    kilometros = Column(String(255), nullable=False)

    # Clave foránea que hace referencia a la tabla Cliente
    id_cliente = Column(Integer, ForeignKey('clientes.id_cliente'))

    # Relacion uno a muchos
    clientes = relationship('Cliente', back_populates='vehiculos')
    ingresos = relationship('Ingreso', back_populates='vehiculos')
    #registros = relationship('Registro', back_populates='vehiculos')


    # Costructor de la clase Vehiculo
    def __init__(self, fecha_alta, marca, modelo, matricula, kilometros):
        '''costructor de la clase Vehiculo'''
        self.fecha_alta = fecha_alta  # Fecha de registro del vehiculo
        self.marca = marca  # marca del vehiculo
        self.modelo = modelo # modelo del vehiculo
        self.matricula = matricula  # matricula del vehiculo
        self.kilometros = kilometros  # kilometros del vehiculo
        print('Vehiculo creado con exito')

    # metodo STR nos muestra la informacion
    def __str__(self):
        return "Vehiculo: id {}, Marca {}, Modelo {}, Matricula {} ".format(self.id_vehiculo, self.marca, self.modelo, self.matricula)


class Recambio(db.Base_mobile):
    '''Clase Recambio
    incluye id_recambio, nombre_recambio, descripcion

    args
    -id_recambio: es un numero integer que compone el código del recambio
    -nombre_recambio: es un string que compone el nombre del recambio
    -descripcion: es un string que compone la descripcion del recambio
    '''

    __tablename__ = 'recambios'
    __table_args__ = {'sqlite_autoincrement': True}

    id_recambio = Column(Integer, primary_key=True, autoincrement=True)
    fecha_alta = Column(DateTime, default=datetime.utcnow)
    nombre_recambio = Column(String(255), nullable=False)
    descripcion = Column(String(255), nullable=False)
    categoria = Column(String(255), nullable=False)
    subcategoria = Column(String(255), nullable=False)

    # Relacion uno a muchos
    registros = relationship('Registro', back_populates='recambios')

    # Costructor de la clase Recambio
    def __init__(self,fecha_alta, nombre_recambio, descripcion, categoria, subcategoria):
        '''costructor de la clase Recambio'''
        self.fecha_alta = fecha_alta  # Fecha de registro del cliente
        self.nombre_recambio = nombre_recambio
        self.descripcion = descripcion
        self.categoria = categoria
        self.subcategoria = subcategoria
        print('recambio creado con exito')

    # metodo STR nos muestra la informacion
    def __str__(self):
        return "Recambio {} con id {} creado con exito".format(self.nombre_recambio, self.id_recambio)


class Ingreso(db.Base_mobile):
    '''Clase Ingreso
    incluye id_ingreso, id_vehiculo, kilometros_ingreso, fecha_ingreso, id_cliente, averia, diagnostico, id_recambio

    args
    -id_ingreso: es un numero integer que compone el codigo del ingreso del vehiculo
    -fecha_ingreso: es un string que indica la fecha del ingreso del vehiculo a taller
    -kilometros_ingreso: es un numero integer que compone los km del vehiculo al momento del ingreso a taller
    -averia: en un string que compone el motivo del ingreso segun el cliente
    -diagnostico: es un string que indica el diagnostico de la averia por el taller
    -id_cliente: es un numero integer que compone el id del cliente del vehiculo ingresado
    -id_vehiculo: es un numero integer que compone el id del vehiculo ingresado a taller
    '''

    __tablename__ = 'ingresos'
    __table_args__ = {'sqlite_autoincrement': True}

    # Estructura de la tabla ingresos
    id_ingreso = Column(Integer, primary_key=True, autoincrement=True)
    fecha_ingreso = Column(DateTime, default=datetime.utcnow)
    kilometros_ingreso = Column(Integer, nullable=False)
    averia = Column(String(255), nullable=False)
    diagnostico = Column(String(255), nullable=False)

    # Relacion clave foranea
    id_cliente = Column(Integer, ForeignKey('clientes.id_cliente'))
    id_vehiculo = Column(Integer, ForeignKey('vehiculos.id_vehiculo'))

    # Relacion uno a muchos
    clientes = relationship('Cliente', back_populates='ingresos')
    vehiculos = relationship('Vehiculo', back_populates='ingresos')
    registros = relationship('Registro', back_populates='ingresos')

    # Costructor de la clase Ingreso
    def __init__(self, kilometros_ingreso, fecha_ingreso, averia, diagnostico):
        '''costructor de la clase Precio'''
        self.fecha_ingreso = fecha_ingreso  # fecha de ingreso del vehiculo al taller
        self.kilometros_ingreso = kilometros_ingreso
        self.averia = averia # motivo del ingreso segun el cliente
        self.diagnostico = diagnostico # diagnostico de la averia por el taller

        print('Ingreso creado con exito')

    # metodo STR nos muestra la informacion
    def __str__(self):
        return "el Vehiculo id {}, del cliente {}, con fecha de ingreso a taller {} ha sido registrado con exito".format(self.id_vehiculo, self.id_cliente, self.fecha_ingreso)


class Registro(db.Base_mobile):
    '''Clase Registro
    incluye id_registro, id_cliente, id_vehiculo, id_ingreso, id_recambio

    args
    -id_registro: es un numero integer que compone el código del registro
    -precio: es un numero flotante que compone el precio de un determinado recambio
    -descuento: es un numero flotante que compone el porcentaje del descuento
    -cantidad: es un numero flotante que compone la cantidad de unidades de un determinado item
    -id_cliente: es un numero integer que compone el codigo del cliente
    -id_vehiculo: es un numero integer que compone el codigo del vehiculo
    -id_ingreso: es un numero integer que compone el codigo del ingreso del vehiculo
    -id_recambio: es un numero integer que compone el código del recambio
    '''

    __tablename__ = 'registros'
    __table_args__ = {'sqlite_autoincrement': True}

    id_registro = Column(Integer, primary_key=True, autoincrement=True)
    precio = Column(Float, nullable=False)
    descuento = Column(Float, nullable=False)
    cantidad = Column(Float, nullable=False)
    costo_real = Column(Float, nullable=False)



    # Relacion clave foranea
    #id_cliente = Column(Integer, ForeignKey('clientes.id_cliente'))
    #id_vehiculo = Column(Integer, ForeignKey('vehiculos.id_vehiculo'))
    id_recambio = Column(Integer, ForeignKey('recambios.id_recambio'))
    id_ingreso = Column(Integer, ForeignKey('ingresos.id_ingreso'))

    # Relacion uno a muchos
    #clientes = relationship('Cliente', back_populates='registros')
    #vehiculos = relationship('Vehiculo', back_populates='registros')
    recambios = relationship('Recambio', back_populates='registros')
    ingresos = relationship('Ingreso', back_populates='registros')

    # Costructor de la clase Registro
    def __init__(self, precio, descuento, cantidad, costo_real):
        '''costructor de la clase Registro'''
        self.precio = precio
        self.descuento = descuento
        self.cantidad = cantidad
        self.costo_real = costo_real
        print('registro creado con exito')

    # metodo STR nos muestra la informacion
    def __str__(self):
        return "Registro {} para vehiculo matricula {} registrado con exito".format(self.id_registro, self.vehiculos.matricula)

