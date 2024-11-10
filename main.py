'''Peace is not found in the absence of storms, but in the ability to dance amidst them'''
import sys
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

    #seleccionamos al cliente
    clientes = db.session.query(Cliente).all()


    if clientes:
        for id, cliente in enumerate(clientes, start=1):
            print(f" ID: {cliente.id_cliente}, Nombre: {cliente.nombre}")

        # pide al usuario que ingrese el ID del cliente
        id_cliente_seleccionado = int(input("Ingresa el ID del cliente: "))

        #verifica si el ID esta dentro del rango valido
        if 1 <= id_cliente_seleccionado <= len(clientes):
            cliente_seleccionado = clientes[id_cliente_seleccionado - 1]
            print(f"Cliente seleccionado: {cliente_seleccionado.nombre}")
        else:
            print("El ID ingresado esta fuera de rango.")

    else:
        print("No hay clientes en la base de datos")


    marca = input("Introduce la marca del vehiculo: ")
    modelo = input("Introduce el modelo del vehiculo: ")
    matricula = input("Introduce la matricula del vehiculo: ")
    kilometros = input("Introduce los kilometros del vehiculo: ")
    fecha_alta = datetime.now()


    # nueva instancia de vehiculos
    nuevo_vehiculo = Vehiculo(marca=marca, modelo=modelo, matricula=matricula, kilometros=kilometros, fecha_alta=fecha_alta)
    db.session.add(nuevo_vehiculo)
    #db.session.commit()


    # relacion bidireccional automatica
    cliente_seleccionado.vehiculos.append(nuevo_vehiculo)
    db.session.commit()
    db.session.close()

# metodo para registrar nuevo recambio
def recambio_nuevo():
    print("\n > Crear recambio")
    nombre_recambio = input("Introduce el nombre del recambio: ")
    descripcion = input("Introduce la descripcion del recambio: ")
    categoria = input("Introduce la categoria del recambio: ")
    subcategoria = input("Introduce la subcategoria del recambio: ")
    fecha_alta = datetime.now()

    # Creación y adición del nuevo cliente
    nuevo_recambio = Recambio(nombre_recambio=nombre_recambio, descripcion=descripcion, categoria = categoria, subcategoria= subcategoria, fecha_alta=fecha_alta)
    db.session.add(nuevo_recambio)
    db.session.commit()
    db.session.close()

# metodo para registrar nuevo ingreso
def ingreso_nuevo(self):
    #global cliente_seleccionado, vehiculo_seleccionado
    print("\n > Crear ingreso")

    # Selección del cliente
    clientes = db.session.query(Cliente).all()

    if clientes:
        for cliente in clientes:
            print(f" ID: {cliente.id_cliente}, Nombre: {cliente.nombre}")

        # Pide al usuario que ingrese el ID del cliente
        id_cliente_seleccionado = int(input("Ingresa el ID del cliente: "))

        # Verifica si el ID está dentro del rango válido
        cliente_seleccionado = None
        for cliente in clientes:
            if cliente.id_cliente == id_cliente_seleccionado:
                cliente_seleccionado = cliente
                break

        if cliente_seleccionado:
            print(f"Cliente seleccionado: {cliente_seleccionado.nombre}")
        else:
            print("El ID ingresado es inválido.")
            return
    else:
        print("No hay clientes en la base de datos.")
        return

    # Realiza búsqueda de los vehículos del cliente seleccionado
    vehiculos = db.session.query(Vehiculo).filter(Vehiculo.id_cliente == cliente_seleccionado.id_cliente).all()

    if vehiculos:
        for vehiculo in vehiculos:
            print(f" ID: {vehiculo.id_vehiculo}, Modelo: {vehiculo.modelo}, Matrícula: {vehiculo.matricula}")

        # Pide al usuario que ingrese el ID del vehículo
        id_vehiculo_seleccionado = int(input("Ingresa el ID del vehículo: "))

        # Verifica si el ID está dentro del rango válido
        vehiculo_seleccionado = None
        for vehiculo in vehiculos:
            if vehiculo.id_vehiculo == id_vehiculo_seleccionado:
                vehiculo_seleccionado = vehiculo
                break

        if vehiculo_seleccionado:
            print(
                f"Vehículo seleccionado: {vehiculo_seleccionado.modelo}, Matrícula: {vehiculo_seleccionado.matricula}")
        else:
            print("El ID ingresado es inválido.")
            return
    else:
        print("No hay vehículos en la base de datos para este cliente.")
        return

    # Datos del ingreso
    kilometros_ingreso = input("Introduce los kilómetros del vehículo: ")
    averia = input("Introduce la avería reportada por el cliente: ")
    diagnostico = input("Introduce el diagnóstico del vehículo por el mecánico: ")
    fecha_ingreso = datetime.now()

    # Nueva instancia de Ingreso
    nuevo_ingreso = Ingreso(kilometros_ingreso=kilometros_ingreso, averia=averia, diagnostico=diagnostico,
                            fecha_ingreso=fecha_ingreso)
    db.session.add(nuevo_ingreso)

    # Relación bidireccional automática
    cliente_seleccionado.ingresos.append(nuevo_ingreso)
    vehiculo_seleccionado.ingresos.append(nuevo_ingreso)

    # Guardar cambios
    db.session.commit()
    db.session.close()
    print("Ingreso creado exitosamente.")

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
            print('Estas en Añadir Vehiculo')
            vehiculo_nuevo()
        elif opcionMenu == '3':
            print('Estas en Añadir Recambio')
            recambio_nuevo()
        elif opcionMenu == '4':
            print('Estas en Añadir Ingreso')
            ingreso_nuevo()
        elif opcionMenu == '5':
            print('Estas en Añadir Registro')
            registro_nuevo()
        elif opcionMenu == '6':
            print('Saliendo del Programa...')
            sys.exit(1)
