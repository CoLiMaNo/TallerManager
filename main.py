'''Peace is not found in the absence of storms, but in the ability to dance amidst them'''

from datetime import datetime
from flet import *
from sqlalchemy import and_, desc, asc
from sqlalchemy.exc import SQLAlchemyError
from models import Cliente, Vehiculo, Recambio, Ingreso, Registro
import db

# metodo para registrar cliente nuevo
def cliente_nuevo():
    print("\n > Crear cliente")
    nombre = input("Introduce el nombre del cliente: ")
    telefono = input("Introduce el telefono: ")
    direccion = input("Introduce la direccion: ")
    correo = input("Introduce el correo: ")
    fecha_alta = datetime.now()

    # Creación y adición del nuevo cliente
    nuevo_cliente = Cliente(nombre=nombre, telefono=telefono, direccion=direccion, correo=correo, fecha_alta=fecha_alta)
    db.session.add(nuevo_cliente)
    db.session.commit()
    db.session.close()

# metodo para registrar nuevo vehiculo
def vehiculo_nuevo():
    print("\n > Crear vehiculo")
    marca = input("Introduce la marca del vehiculo: ")
    modelo = input("Introduce el modelo del vehiculo: ")
    matricula = input("Introduce la matricula del vehiculo: ")
    kilometros = input("Introduce los kilometros del vehiculo: ")
    fecha_alta = datetime.now()

    # Creación y adición del nuevo vehiculo
    nuevo_vehiculo = Vehiculo(marca=marca, modelo=modelo, matricula=matricula, kilometros=kilometros, fecha_alta=fecha_alta)
    db.session.add(nuevo_vehiculo)
    db.session.commit()
    db.session.close()

# metodo para registrar nuevo recambio
def recambio_nuevo():
    print("\n > Crear recambio")
    nombre_recambio = input("Introduce el nombre del recambio: ")
    descripcion = input("Introduce la descripcion del recambio: ")
    fecha_alta = datetime.now()

    # Creación y adición del nuevo cliente
    nuevo_recambio = Recambio(nombre_recambio=nombre_recambio, descripcion=descripcion, fecha_alta=fecha_alta)
    db.session.add(nuevo_recambio)
    db.session.commit()
    db.session.close()

# metodo para registrar nuevo ingreso
def ingreso_nuevo():
    pass

# metodo para registrar nuevo ingreso
def registro_nuevo():
    pass


if __name__ == '__main__':

    # Resetea la base de datos si existe
    # db.Base_mobile.metadata.drop_all(bind=db.engine_sqlite, checkfirst=True)

    # crea si no existen las tablas de todos los modelos que encuentre en models.py
    db.Base_mobile.metadata.create_all(db.engine_sqlite) # Base de datos Mobil

    print('Bienvenido, Elije una opcion del Menu')
    while True:

        print('''
            1. Añadir Cliente
            2. Añadir Vehiculo
            3. Añadir Recambio
            4. Añadir Ingreso
            5. Añadir Registro
            6. Salir
            ''')

        opcionMenu = input('Introduce una opcion:')
        if opcionMenu == '1':
            print('Estas en Añadir Cliente')
            cliente_nuevo()
        elif opcionMenu == '2':
            print('Estas en Añadir Cliente')
            vehiculo_nuevo()
        elif opcionMenu == '3':
            print('Estas en Añadir Recambio')
            recambio_nuevo()
        elif opcionMenu == '3':
            print('Estas en Añadir Ingreso')
            ingreso_nuevo()
        elif opcionMenu == '3':
            print('Estas en Añadir Registro')
            registro_nuevo()
