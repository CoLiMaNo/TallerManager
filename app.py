import datetime
import flet as ft
from flet import *
from sqlalchemy import and_, desc, asc, or_
from sqlalchemy.exc import SQLAlchemyError
from models import Cliente, Vehiculo, Recambio, Ingreso, Registro
import db
import os


class VentanaInicio(ft.View):
    '''Clase VentanaInicio: Interfaz para ventana de inicio.

    Args:
        - page: Instancia de la pagina actual.

    Contiene:
        - Boton ElevatedButton: para moverte a Clientes.
        - Boton ElevatedButton: para moverte a Vehiculos.
        - Boton ElevatedButton: para moverte a Recambios.
        - Boton ElevatedButton: para moverte a Ingresos.
        '''

    def __init__(self, page: ft.Page):
        '''Constructor de la interfaz grafica para la ventana Inicio'''
        super(VentanaInicio, self).__init__(
            route="/inicio", horizontal_alignment=CrossAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER
        )

        self.page = page

        # Color de fondo contenedor principal
        self.bgcolor = "#FAFAF3"

        # Logo de la App
        self.logo = ft.Container(
            ft.Container(
                bgcolor="#f6f6f6",
                width=250,
                height=90,
                padding=0,
                image_repeat=ImageRepeat.NO_REPEAT,
                shape=ft.BoxShape("rectangle"),
                # Define imagen
                image_src="/logo-taller4.png",
                image_fit=ft.ImageFit.COVER,
            ),
            alignment=ft.alignment.Alignment(x=0, y=0)
        )

        # Imagen vehiculo
        self.ImagenVehiculo = ft.Container(
            ft.Container(
                bgcolor="#f6f6f6",
                width=200,
                height=90,
                padding=0,
                image_repeat=ImageRepeat.NO_REPEAT,
                shape=ft.BoxShape("rectangle"),
                # Define imagen
                image_src="/ImagenVehiculo.png",
                image_fit=ft.ImageFit.COVER,
            ),
            alignment=ft.alignment.Alignment(x=0, y=0)
        )

        # Boton para moverte a clientes
        self.boton_clientes = ft.Container(
            ft.ElevatedButton(
                text="Clientes",
                color="white",
                bgcolor="#12597b",
                # icon=icons.LOGIN,
                # icon_color="333333",
                width=150,
                height=30,
                on_click=lambda _: page.go("/clientes")
            ),
            alignment=ft.alignment.Alignment(x=0, y=0)
        )

        # Boton para moverte a vehiculos
        self.boton_vehiculos = ft.Container(
            ft.ElevatedButton(
                text="Vehiculos",
                color="white",
                bgcolor="#12597b",
                # icon=icons.LOGIN,
                # icon_color="333333",
                width=150,
                height=30,
                on_click=lambda _: page.go("/vehiculos")

            ),
            alignment=ft.alignment.Alignment(x=0, y=0)
        )

        # Boton para moverte a recambios
        self.boton_recambios = ft.Container(
            ft.ElevatedButton(
                text="Recambios",
                color="white",
                bgcolor="#12597b",
                # icon=icons.LOGIN,
                # icon_color="333333",
                width=150,
                height=30,
                on_click=lambda _: page.go("/recambios")
            ),
            alignment=ft.alignment.Alignment(x=0, y=0)
        )

        # Boton para moverte a ingresos
        self.boton_ingresos = ft.Container(
            ft.ElevatedButton(
                text="Ingresos",
                color="white",
                bgcolor="#12597b",
                # icon=icons.LOGIN,
                # icon_color="333333",
                width=150,
                height=30,
                on_click=lambda _: page.go("/ingresos")
            ),
            alignment=ft.alignment.Alignment(x=0, y=0)
        )

        # imagen clientes
        self.ImagenClientes = ft.Container(
            ft.Container(
                bgcolor="#f6f6f6",
                width=200,
                height=90,
                padding=0,
                image_repeat=ImageRepeat.NO_REPEAT,
                shape=ft.BoxShape("rectangle"),
                # Define imagen
                image_src="/ImagenClientes.png",
                image_fit=ft.ImageFit.COVER,
            ),
            alignment=ft.alignment.Alignment(x=0, y=0)
        )

        # imagen recambios
        self.ImagenRecambios = ft.Container(
            ft.Container(
                bgcolor="#f6f6f6",
                width=200,
                height=90,
                padding=0,
                image_repeat=ImageRepeat.NO_REPEAT,
                shape=ft.BoxShape("rectangle"),
                # Define imagen
                image_src="/ImagenRecambios.png",
                image_fit=ft.ImageFit.COVER,
            ),
            alignment=ft.alignment.Alignment(x=0, y=0)
        )

        # imagen ingresos
        self.Imagen_de_Ingresos = ft.Container(
            ft.Container(
                bgcolor="#f6f6f6",
                width=200,
                height=90,
                padding=0,
                image_repeat=ImageRepeat.NO_REPEAT,
                shape=ft.BoxShape("rectangle"),
                # Define imagen
                image_src="/Imagen_de_Ingresos.png",
                image_fit=ft.ImageFit.COVER,
            ),
            alignment=ft.alignment.Alignment(x=0, y=0)
        )

        # Marcas vehiculos
        self.marcas = ft.Container(
            ft.Row([
                ft.Container(
                    bgcolor="#FAFAF3",
                    width=65,
                    height=65,
                    image_repeat=ImageRepeat.NO_REPEAT,
                    shape=ft.BoxShape("rectangle"),
                    # Define imagen
                    image_src="/Toyota-Logo.png",
                    image_fit=ft.ImageFit.SCALE_DOWN
                ),
                ft.Container(
                    bgcolor="#FAFAF3",
                    width=70,
                    height=70,
                    image_repeat=ImageRepeat.NO_REPEAT,
                    shape=ft.BoxShape("rectangle"),
                    # Define la imagen
                    image_src="/Mercedes-Benz-Logo.png",
                    image_fit=ft.ImageFit.SCALE_DOWN
                ),
                ft.Container(
                    bgcolor="#FAFAF3",
                    width=65,
                    height=65,
                    image_repeat=ImageRepeat.NO_REPEAT,
                    shape=ft.BoxShape("rectangle"),
                    # Define la imagen
                    image_src="/Audi-Logo.png",
                    image_fit=ft.ImageFit.SCALE_DOWN
                ),
            ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,

            )
        )

        # Marcas vehiculos
        self.marcas2 = ft.Container(
            ft.Row([
                ft.Container(
                    bgcolor="#FAFAF3",
                    width=70,
                    height=70,
                    image_repeat=ImageRepeat.NO_REPEAT,
                    shape=ft.BoxShape("rectangle"),
                    # Define la imagen
                    image_src="/Nissan-Logo.png",
                    image_fit=ft.ImageFit.SCALE_DOWN
                ),
                ft.Container(
                    bgcolor="#FAFAF3",
                    width=70,
                    height=70,
                    image_repeat=ImageRepeat.NO_REPEAT,
                    shape=ft.BoxShape("rectangle"),
                    # Define la imagen
                    image_src="/Logo-Honda.png",
                    image_fit=ft.ImageFit.SCALE_DOWN
                ),
                ft.Container(
                    bgcolor="#FAFAF3",
                    width=65,
                    height=65,
                    image_repeat=ImageRepeat.NO_REPEAT,
                    shape=ft.BoxShape("rectangle"),
                    # Define imagen
                    image_src="/Hyundai-Logo.png",
                    image_fit=ft.ImageFit.SCALE_DOWN
                ),

            ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,

            )
        )

        # Marcas vehiculos
        self.marcas3 = ft.Container(
            ft.Row([
                ft.Container(
                    bgcolor="#FAFAF3",
                    width=65,
                    height=65,
                    image_repeat=ImageRepeat.NO_REPEAT,
                    shape=ft.BoxShape("rectangle"),
                    # Define la imagen
                    image_src="/Volkswagen-Logo.png",
                    image_fit=ft.ImageFit.SCALE_DOWN
                ),
                ft.Container(
                    bgcolor="#FAFAF3",
                    width=65,
                    height=65,
                    image_repeat=ImageRepeat.NO_REPEAT,
                    shape=ft.BoxShape("rectangle"),
                    # Define la imagen
                    image_src="/Ford-Logo.png",
                    image_fit=ft.ImageFit.SCALE_DOWN
                ),
                ft.Container(
                    bgcolor="#FAFAF3",
                    width=65,
                    height=65,
                    image_repeat=ImageRepeat.NO_REPEAT,
                    shape=ft.BoxShape("rectangle"),
                    # Define imagen
                    image_src="/Kia-Logo.png",
                    image_fit=ft.ImageFit.SCALE_DOWN
                ),

            ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,

            )
        )

        # Contenedor principal que contiene todos los elementos de la interfaz
        self.controls = [
            ft.Container(
                ft.Column([
                    ft.Divider(height=10, color="transparent"),
                    self.logo,
                    ft.Divider(height=10, color="transparent"),
                    self.ImagenVehiculo, ft.Divider(height=10, color="transparent"),
                    # ft.Divider(height=10, color="#E0E0E0"),
                    self.boton_clientes,
                    self.boton_vehiculos,
                    self.boton_recambios,
                    self.boton_ingresos,
                ]
                ),

                # propiedades contenedor principal
                border_radius=25,
                width=350,  # ancho
                height=655,  # Alto
                gradient=ft.LinearGradient([  # color del contenedor configurable en 2 tonos de color
                    "#FAFAF3",
                    "#FAFAF3",
                ])

            )
        ]


class VentanaCliente(ft.View):
    '''Clase VentanaInicio: Interfaz para ventana de clientes.

    Args:
        - page: Instancia de la pagina actual.

    Contiene:
        - Imagen de Clientes como titulo.
        - Input para ingresar busqueda.
        - Boton ElevatedButton: para activar la busqueda.
        - Boton ElevatedButton: para añadir cliente nuevo.
        - Boton ElevatedButton: para modificar cliente.
        - Boton ElevatedButton: para eliminar cliente.
        '''

    def __init__(self, page: ft.Page):
        '''Constructor de la interfaz grafica para la ventana Clientes'''
        super(VentanaCliente, self).__init__(
            route="/clientes", horizontal_alignment=CrossAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER
        )

        self.page = page

        # Color de fondo contenedor principal
        self.bgcolor = "#FAFAF3"

        # Imagen clientes
        self.imagenClientes = ft.Container(
            ft.Container(
                bgcolor="#f6f6f6",
                width=320,
                height=90,
                padding=0,
                image_repeat=ImageRepeat.NO_REPEAT,
                shape=ft.BoxShape("rectangle"),
                # Define imagen
                image_src="/ImagenClientes.png",
                image_fit=ft.ImageFit.COVER,
            ),
            alignment=ft.alignment.Alignment(x=0, y=0)
        )

        # Campo de entrada para la busqueda
        self.input_buscar = ft.TextField(
            label="Buscar Cliente...",
            label_style=TextStyle(color='#6a6965', size=12),
            value="",
            border_radius=ft.border_radius.vertical(top=0, bottom=0),
            hint_text="Introduce el nombre del cliente",
            hint_style=TextStyle(color='#6a6965', size=10),
            color='black',
            height=40,
            cursor_color="#12597b",
            text_size=13,
            border_color="#12597b",
            autofocus=True,
            bgcolor="#E1F5FE"
        )

        # Boton para activar la busqueda del cliente
        self.BotonBuscarCliente = ft.Container(
            ft.ElevatedButton(
                text="Buscar Cliente",
                color="white",
                bgcolor="#12597b",
                # icon=icons.LOGIN,
                # icon_color="333333",
                width=180,
                height=50,
                on_click=lambda _: page.go("/inicio")
            ),
            alignment=ft.alignment.Alignment(x=0, y=1)
        )

        # Barra de navegacion
        self.barraNavegacion = ft.NavigationBar(
            selected_index=0,
            # on_change=lambda e: self.on_navigation_change(e),
            destinations=[
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.HOME_OUTLINED,
                        color=ft.colors.GREY_900,
                        size=20  # Ajusta el tamaño del ícono no seleccionado
                    ),
                    selected_icon_content=ft.Icon(
                        name=ft.icons.HOME_ROUNDED,
                        color="#12597b",
                        size=24  # Ajusta el tamaño del ícono seleccionado
                    ),
                    label="Inicio",
                ),
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.PERSON_OUTLINED,
                        color=ft.colors.BLUE_GREY_900,
                        size=20
                    ),
                    selected_icon_content=ft.Icon(
                        name=ft.icons.PERSON,
                        color="#12597b",
                        size=24
                    ),
                    label="Cliente",

                ),
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.DIRECTIONS_CAR_OUTLINED,
                        color=ft.colors.BLUE_GREY_900,
                        size=20
                    ),
                    selected_icon_content=ft.Icon(
                        name=ft.icons.DIRECTIONS_CAR,
                        color="#12597b",
                        size=24
                    ),
                    label="Vehículo",
                ),
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.SETTINGS_OUTLINED,
                        color=ft.colors.BLUE_GREY_900,
                        size=20
                    ),
                    selected_icon_content=ft.Icon(
                        name=ft.icons.SETTINGS,
                        color="#12597b",
                        size=24
                    ),
                    label="Recambio",
                ),
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.CAR_REPAIR_OUTLINED,
                        color=ft.colors.BLUE_GREY_900,
                        size=20
                    ),
                    selected_icon_content=ft.Icon(
                        name=ft.icons.CAR_REPAIR,
                        color="#12597b",
                        size=24
                    ),
                    label="Ingreso",
                )
            ],
            bgcolor=ft.colors.GREY_400,  # Color de fondo de la barra de navegación (azul oscuro)
            indicator_color=ft.colors.AMBER_500,  # Color del indicador del destino seleccionado (ámbar)
            surface_tint_color=ft.colors.BLUE_GREY_900,  # Color de superficie para el material (cyan claro)
            label_behavior=ft.NavigationBarLabelBehavior.ONLY_SHOW_SELECTED  # Mostrar la etiqueta  seleccionada
        )

        # Contenedor que contiene el boton de busqueda y las opciones
        self.boton_Y_opciones = ft.Container(
            alignment=ft.alignment.Alignment(x=0, y=0),
            content=Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    # Menu desplegable para elegir ubicacion
                    ft.Dropdown(
                        label='Elige una Opcion',
                        label_style=TextStyle(color='#6a6965', size=12, weight=ft.FontWeight.W_600),
                        height=40,
                        width=200,
                        content_padding=15,
                        color='#333333',
                        border_color="#12597b",
                        text_size=12,
                        on_change=lambda e: self.pestaniaOpcion(e),
                        options=[
                            ft.dropdown.Option("Clientes"),
                            ft.dropdown.Option("Vehiculos"),
                            ft.dropdown.Option("Recambios"),
                            ft.dropdown.Option("Ingresos"),
                        ],
                        bgcolor="#E1F5FE"
                    ),
                    # Boton de busqueda
                    ft.IconButton(
                        content=ft.Image(src="imagenes/buscadorLupa.png", height=40, width=40),
                        icon_color="#AABE89",
                        tooltip='Buscar',

                        on_click=lambda e: self.botonBuscar(e),
                    )
                ]
            )
        )

        # Contenedor para mostrar los resultados de busqueda
        self.vistaResultadosBusqueda = ft.Container(
            bgcolor='#FAFAF3',
            expand=True,
            content=ft.GridView(
                expand=1,
                child_aspect_ratio=1.0,
                runs_count=2,
                spacing=1,
                run_spacing=1,
            )
        )

        # Contenedor principal que contiene todos los elementos de la interfaz
        self.controls = [
            ft.Container(
                ft.Column([
                    # self.tituloClientes,
                    self.imagenClientes,
                    self.input_buscar,
                    self.BotonBuscarCliente,
                    self.vistaResultadosBusqueda,
                    self.barraNavegacion,

                ]
                ),

                # propiedades contenedor principal
                border_radius=25,
                width=350,  # ancho
                height=655,  # Alto
                gradient=ft.LinearGradient([  # color del contenedor configurable en 2 tonos de color
                    "#FAFAF3",
                    "#FAFAF3",
                ])

            )
        ]

    def pestaniaOpcion(self, e):
        try:
            # Crear un objeto Text para mostrar la opcion elegida
            t = ft.Text()

            # Obtener la opcion elegida del menu desplegable
            elegirOpcion = self.boton_Y_opciones.content.controls[0].value

            # Actualizar el valor del objeto Text con la opcion elegida
            t.value = f"Opción elegida: {elegirOpcion}"

            # Diccionario que mapea las opciones a las acciones correspondientes
            acciones = {
                'Clientes': 'Buscar en Clientes',
                'Vehiculos': 'Buscar en Vehiculos',
                'Recambios': 'Buscar en Recambios',
                'Ingresos': 'Buscar en Ingresos',
            }

            # Imprimir un mensaje según la opcion elegida
            if elegirOpcion in acciones:
                print(acciones[elegirOpcion])
            else:
                print('Opción no válida')

            # Actualizar la pagina con el objeto Text
            self.page.update(self)
            # Agregar el objeto Text a la pagina
            self.page.add(t)

        except Exception as e:
            print(f'Error: {e}')
            # Registrar el error en el archivo de texto
            with open("errores.txt", "a") as file:
                momentoEspecificoError = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                nombre_metodo = "pestaniaOpcion, VentanaBuscar"
                mensaje_error = f"{momentoEspecificoError} - Método: {nombre_metodo} - Error general: {e}\n"
                file.write(mensaje_error)
        finally:
            db.session.close()

    # metodo para manejar el evento de clic del boton de busqueda
    def botonBuscar(self, e):
        try:
            tipo_busqueda = self.boton_Y_opciones.content.controls[0].value

            # Realizar la búsqueda segun la ubicacion seleccionada
            if tipo_busqueda in ('Clientes, Vehiculos, Recambios, Ingresos'):
                self.buscarPorOpcion(e)
            else:
                print('Opción no válida, elige una opcion en el desplegable')

        # control de excepciones
        except Exception as e:
            print(f'Error: {e}')
            # Registrar el error en el archivo de texto
            with open("errores.txt", "a") as file:
                momentoEspecificoError = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                nombre_metodo = "botonBuscar, VentanaCliente"
                mensaje_error = f"{momentoEspecificoError} - Método: {nombre_metodo} - Error general: {e}\n"
                file.write(mensaje_error)
        finally:
            db.session.close()

    # metodo para buscar por opcion
    # metodo para buscar el producto por ubicacion y precio asociado
    def buscarPorOpcion(self, e):
        try:
            print("\n > Buscar por Opcion")
            # Limpia los controles actuales del GridView
            self.vistaResultadosBusqueda.content.controls = []

            # input donde el usuario ingresa lo que quiere buscar
            nombreDeLaBusqueda = self.input_buscar.value  # este es el Input

            # ubicacion seleccionada por el usuario
            opcion_seleccionada = self.boton_Y_opciones.content.controls[0].value

            # Buscamos el producto por nombre y ubicacion (ignorando mayúsculas y minusculas)
            nombre_consultaDeLaBusqueda = db.session.query(Cliente, Vehiculo, Recambio, Ingreso).filter(
                or_(
                    Cliente.nombre.ilike(f'%{nombreDeLaBusqueda}%'),
                    Vehiculo.marca.ilike(f'%{nombreDeLaBusqueda}%'),
                    Recambio.descripcion.ilike(f'%{nombreDeLaBusqueda}%'),
                    Ingreso.concepto.ilike(f'%{nombreDeLaBusqueda}%')
                )
            ).all()

            self.input_buscar.value = ""
            self.input_buscar.update()

            if nombre_consultaDeLaBusqueda:
                for producto in nombre_consultaDeLaBusqueda:
                    # Mostramos detalles del producto encontrado
                    print(f"->Nombre: {producto.nombre_producto}."
                          f"\n->Marca: {producto.marca_producto}."
                          f"\n->Descripción: {producto.descripcion_producto}.")

                    # Verificamos si el producto tiene precios asociados
                    if producto.precios:
                        # Filtramos los precios por ubicación
                        precios_ubicacion = [precio for precio in producto.precios if
                                             precio.supermercados.ubicacion == opcion_seleccionada]

                        if precios_ubicacion:
                            # Mostramos los precios asociados al producto con su nombre, marca y descripcion en la ubicación seleccionada
                            print("\nPrecios asociados en la ubicación seleccionada:")
                            for precio in precios_ubicacion:
                                print(f" {producto.nombre_producto}, "
                                      f" {producto.marca_producto}, "
                                      f" {producto.descripcion_producto}, "
                                      f" {precio.precio} €, {precio.supermercados.nombre}, "
                                      f"Ubicación: {opcion_seleccionada}")

                            # Crear una lista de Cards para los resultados de busqueda
                            cards = []
                            for precio in precios_ubicacion:  # Iterar sobre los precios asociados
                                # Crear una Card para cada precio asociado al producto
                                card = ft.Card(
                                    content=ft.Container(
                                        bgcolor="transparent",
                                        image_repeat=ImageRepeat.NO_REPEAT,
                                        image_src="/compras_supermercado4.png",
                                        image_fit=ft.ImageFit.COVER,
                                        image_opacity=0.1,
                                        content=ft.Column(
                                            [
                                                ft.Row([
                                                    ft.Text(f"{producto.nombre_producto}",
                                                            weight=ft.FontWeight.W_700,
                                                            size=10,
                                                            color="#835D84",
                                                            text_align=ft.TextAlign.START),
                                                ]
                                                ),
                                                ft.Text(f"{producto.marca_producto}",
                                                        weight=ft.FontWeight.W_700,
                                                        size=10,
                                                        color="#835D84",
                                                        text_align=ft.TextAlign.START),
                                                ft.Text(f" {producto.descripcion_producto}",
                                                        weight=ft.FontWeight.W_700,
                                                        size=10,
                                                        color="#835D84",
                                                        text_align=ft.TextAlign.START),
                                                ft.Text(f" {precio.precio} €, {precio.supermercados.nombre}",
                                                        weight=ft.FontWeight.W_700,
                                                        size=10,
                                                        color="#835D84",
                                                        text_align=ft.TextAlign.START),
                                                ft.Row(
                                                    [
                                                        ft.PopupMenuButton(
                                                            ft.Icon(name=ft.icons.PLAYLIST_ADD,
                                                                    tooltip='Crear una lista',
                                                                    color="#FF7F50",
                                                                    size=25,
                                                                    ),
                                                            items=[
                                                                ft.PopupMenuItem(
                                                                    # checked=False,
                                                                    on_click=lambda _: self.page.go("/crearlista"),
                                                                    content=Row([
                                                                        ft.Icon(name=ft.icons.PLAYLIST_ADD_CHECK,
                                                                                color=ft.colors.GREEN,
                                                                                size=25,
                                                                                ),
                                                                        ft.Text("Crear una lista",
                                                                                size=12,
                                                                                text_align=ft.TextAlign.START,
                                                                                color=ft.colors.GREY_900),

                                                                    ]))
                                                            ]
                                                        )
                                                    ],
                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                    vertical_alignment=ft.CrossAxisAlignment.START,
                                                ),
                                            ],
                                        ),
                                        padding=10,  # Relleno interior del contenedor
                                        alignment=ft.alignment.center,
                                        border=ft.border.all(1, ft.colors.GREEN_200),
                                        border_radius=ft.border_radius.all(10),
                                    )
                                )

                                cards.append(card)

                            # Agregar las Cards al GridView
                            for card in cards:
                                self.vistaResultadosBusqueda.content.controls.append(card)
                            # Actualizar la interfaz de usuario
                            self.vistaResultadosBusqueda.update()
                        else:
                            print(f"No hay precios asociados en la ubicación '{opcion_seleccionada}'.")
                    else:
                        print("El producto no tiene precios asociados.")
            else:
                print(f"No se encontró ningún producto con el nombre '{nombreDeLaBusqueda}'.")

                # Cerramos la sesion de la base de datos
                db.session.close()

        # control de excepciones
        except SQLAlchemyError as e:
            print(type(e).__name__)
            print("Error de base de datos:", e)
            db.session.rollback()  # Deshacer cualquier cambio pendiente en la base de datos en caso de error
            # Registrar el error en un archivo de texto
            with open("errores.txt", "a") as file:  # Abrir el archivo en modo de escritura, 'a' para añadir al final
                momentoEspecificoError = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                nombre_metodo = "buscarPrecioUbicacion, VentanaBuscar"
                mensaje_error = f"{momentoEspecificoError} - Método: {nombre_metodo} - Error general: {e}\n"
                file.write(mensaje_error)
        except Exception as e:
            print(type(e).__name__)
            print(e)
            with open("errores.txt", "a") as file:  # Abrir el archivo en modo de escritura, 'a' para añadir al final
                momentoEspecificoError = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                nombre_metodo = "buscarPrecioUbicacion, VentanaBuscar"
                mensaje_error = f"{momentoEspecificoError} - Método: {nombre_metodo} - Error general: {e}\n"
                file.write(mensaje_error)
        finally:
            db.session.close()


class VentanaVehiculo(ft.View):
    '''Clase VentanaVehiculo: Interfaz para ventana de vehiculos.

    Args:
        - page: Instancia de la pagina actual.

    Contiene:
        - Imagen de Vehiculos como titulo.
        - Input para ingresar busqueda.
        - Boton ElevatedButton: para activar la busqueda.
        - Boton ElevatedButton: para añadir vehiculo nuevo.
        - Boton ElevatedButton: para modificar vehiculo.
        - Boton ElevatedButton: para eliminar vehiculo.
        '''

    def __init__(self, page: ft.Page):
        '''Constructor de la interfaz grafica para la ventana Vehiculos'''
        super(VentanaVehiculo, self).__init__(
            route="/vehiculos", horizontal_alignment=CrossAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER
        )

        self.page = page

        # Color de fondo contenedor principal
        self.bgcolor = "#FAFAF3"

        # Titulo con imagen vehiculo
        self.imagenVehiculos = ft.Container(
            ft.Container(
                bgcolor="#f6f6f6",
                width=320,
                height=90,
                padding=0,
                image_repeat=ImageRepeat.NO_REPEAT,
                shape=ft.BoxShape("rectangle"),
                # Define imagen
                image_src="/ImagenVehiculos.png",
                image_fit=ft.ImageFit.COVER,
            ),
            alignment=ft.alignment.Alignment(x=0, y=0)
        )

        # Campo de entrada para la busqueda
        self.input_buscar = ft.TextField(
            label="Buscar Vehiculo...",
            label_style=TextStyle(color='#6a6965', size=12),
            value="",
            border_radius=ft.border_radius.vertical(top=0, bottom=0),
            hint_text="Introduce la matricula del vehiculo",
            hint_style=TextStyle(color='#6a6965', size=10),
            color='black',
            height=40,
            cursor_color="#12597b",
            text_size=13,
            border_color="#12597b",
            autofocus=True,
            bgcolor="#E1F5FE"
        )

        # Boton para activar la busqueda del vehiculo
        self.BotonBuscarVehiculo = ft.Container(
            ft.ElevatedButton(
                text="Buscar Vehiculo",
                color="white",
                bgcolor="#12597b",
                # icon=icons.LOGIN,
                # icon_color="333333",
                width=180,
                height=50,
                on_click=lambda _: page.go("/inicio")
            ),
            alignment=ft.alignment.Alignment(x=0, y=1)
        )

        # Barra de navegacion
        self.barraNavegacion = ft.NavigationBar(
            selected_index=0,
            # on_change=lambda e: self.on_navigation_change(e),
            destinations=[
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.HOME_OUTLINED,
                        color=ft.colors.GREY_900,
                        size=20  # Ajusta el tamaño del ícono no seleccionado
                    ),
                    selected_icon_content=ft.Icon(
                        name=ft.icons.HOME_ROUNDED,
                        color="#12597b",
                        size=24  # Ajusta el tamaño del ícono seleccionado
                    ),
                    label="Inicio",
                ),
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.PERSON_OUTLINED,
                        color=ft.colors.BLUE_GREY_900,
                        size=20
                    ),
                    selected_icon_content=ft.Icon(
                        name=ft.icons.PERSON,
                        color="#12597b",
                        size=24
                    ),
                    label="Cliente",

                ),
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.DIRECTIONS_CAR_OUTLINED,
                        color=ft.colors.BLUE_GREY_900,
                        size=20
                    ),
                    selected_icon_content=ft.Icon(
                        name=ft.icons.DIRECTIONS_CAR,
                        color="#12597b",
                        size=24
                    ),
                    label="Vehículo",
                ),
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.SETTINGS_OUTLINED,
                        color=ft.colors.BLUE_GREY_900,
                        size=20
                    ),
                    selected_icon_content=ft.Icon(
                        name=ft.icons.SETTINGS,
                        color="#12597b",
                        size=24
                    ),
                    label="Recambio",
                ),
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.CAR_REPAIR_OUTLINED,
                        color=ft.colors.BLUE_GREY_900,
                        size=20
                    ),
                    selected_icon_content=ft.Icon(
                        name=ft.icons.CAR_REPAIR,
                        color="#12597b",
                        size=24
                    ),
                    label="Ingreso",
                )
            ],
            bgcolor=ft.colors.GREY_400,  # Color de fondo de la barra de navegación (azul oscuro)
            indicator_color=ft.colors.AMBER_500,  # Color del indicador del destino seleccionado (ámbar)
            surface_tint_color=ft.colors.BLUE_GREY_900,  # Color de superficie para el material (cyan claro)
            label_behavior=ft.NavigationBarLabelBehavior.ONLY_SHOW_SELECTED  # Mostrar la etiqueta  seleccionada
        )

        # Contenedor para mostrar los resultados de busqueda
        self.vistaResultadosBusqueda = ft.Container(
            bgcolor='#FAFAF3',
            expand=True,
            content=ft.GridView(
                expand=1,
                child_aspect_ratio=1.0,
                runs_count=2,
                spacing=1,
                run_spacing=1,
            )
        )

        # Contenedor principal que contiene todos los elementos de la interfaz
        self.controls = [
            ft.Container(
                ft.Column([
                    self.imagenVehiculos,
                    self.input_buscar,
                    self.BotonBuscarVehiculo,
                    self.vistaResultadosBusqueda,
                    self.barraNavegacion,
                ]
                ),

                # propiedades contenedor principal
                border_radius=25,
                width=350,  # ancho
                height=655,  # Alto
                gradient=ft.LinearGradient([  # color del contenedor configurable en 2 tonos de color
                    "#FAFAF3",
                    "#FAFAF3",
                ])

            )
        ]

        # metodo de navegacion para la barra de navegacion


class VentanaRecambios(ft.View):
    '''Clase VentanaVehiculo: Interfaz para ventana de recambios.

    Args:
        - page: Instancia de la pagina actual.

    Contiene:
        - Imagen de Recambios como titulo.
        - Input para ingresar busqueda.
        - Boton ElevatedButton: para activar la busqueda.
        - Boton ElevatedButton: para añadir recambio nuevo.
        - Boton ElevatedButton: para modificar recambio.
        - Boton ElevatedButton: para eliminar recambio.
        '''

    def __init__(self, page: ft.Page):
        '''Constructor de la interfaz grafica para la ventana recambios'''
        super(VentanaRecambios, self).__init__(
            route="/recambios", horizontal_alignment=CrossAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER
        )

        self.page = page

        # Color de fondo contenedor principal
        self.bgcolor = "#FAFAF3"

        # Titulo imagen recambios
        self.imagenRecambios = ft.Container(
            ft.Container(
                bgcolor="#f6f6f6",
                width=320,
                height=90,
                padding=0,
                image_repeat=ImageRepeat.NO_REPEAT,
                shape=ft.BoxShape("rectangle"),
                # Define imagen
                image_src="/ImagenRecambios.png",
                image_fit=ft.ImageFit.COVER,
            ),
            alignment=ft.alignment.Alignment(x=0, y=0)
        )

        # Campo de entrada para la busqueda
        self.input_buscarRecambio = ft.TextField(
            label="Buscar Recambio...",
            label_style=TextStyle(color='#6a6965', size=12),
            value="",
            border_radius=ft.border_radius.vertical(top=0, bottom=0),
            hint_text="Introduce el recambio",
            hint_style=TextStyle(color='#6a6965', size=10),
            color='black',
            height=40,
            cursor_color="#12597b",
            text_size=13,
            border_color="#12597b",
            autofocus=True,
            bgcolor="#E1F5FE"
        )

        # Boton de buscar recambio
        self.BotonBuscarRecambio = ft.Container(
            ft.ElevatedButton(
                text="Buscar Recambio",
                color="white",
                bgcolor="#12597b",
                # icon=icons.LOGIN,
                # icon_color="333333",
                width=180,
                height=50,
                on_click=lambda _: page.go("/inicio")
            ),
            alignment=ft.alignment.Alignment(x=0, y=1)
        )

        # Barra de navegacion
        self.barraNavegacion = ft.NavigationBar(
            selected_index=0,
            # on_change=lambda e: self.on_navigation_change(e),
            destinations=[
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.HOME_OUTLINED,
                        color=ft.colors.GREY_900,
                        size=20  # Ajusta el tamaño del ícono no seleccionado
                    ),
                    selected_icon_content=ft.Icon(
                        name=ft.icons.HOME_ROUNDED,
                        color="#12597b",
                        size=24  # Ajusta el tamaño del ícono seleccionado
                    ),
                    label="Inicio",
                ),
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.PERSON_OUTLINED,
                        color=ft.colors.BLUE_GREY_900,
                        size=20
                    ),
                    selected_icon_content=ft.Icon(
                        name=ft.icons.PERSON,
                        color="#12597b",
                        size=24
                    ),
                    label="Cliente",

                ),
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.DIRECTIONS_CAR_OUTLINED,
                        color=ft.colors.BLUE_GREY_900,
                        size=20
                    ),
                    selected_icon_content=ft.Icon(
                        name=ft.icons.DIRECTIONS_CAR,
                        color="#12597b",
                        size=24
                    ),
                    label="Vehículo",
                ),
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.SETTINGS_OUTLINED,
                        color=ft.colors.BLUE_GREY_900,
                        size=20
                    ),
                    selected_icon_content=ft.Icon(
                        name=ft.icons.SETTINGS,
                        color="#12597b",
                        size=24
                    ),
                    label="Recambio",
                ),
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.CAR_REPAIR_OUTLINED,
                        color=ft.colors.BLUE_GREY_900,
                        size=20
                    ),
                    selected_icon_content=ft.Icon(
                        name=ft.icons.CAR_REPAIR,
                        color="#12597b",
                        size=24
                    ),
                    label="Ingreso",
                )
            ],
            bgcolor=ft.colors.GREY_400,  # Color de fondo de la barra de navegación (azul oscuro)
            indicator_color=ft.colors.AMBER_500,  # Color del indicador del destino seleccionado (ámbar)
            surface_tint_color=ft.colors.BLUE_GREY_900,  # Color de superficie para el material (cyan claro)
            label_behavior=ft.NavigationBarLabelBehavior.ONLY_SHOW_SELECTED  # Mostrar la etiqueta  seleccionada
        )

        # Contenedor para mostrar los resultados de busqueda
        self.vistaResultadosBusqueda = ft.Container(
            bgcolor='#FAFAF3',
            expand=True,
            content=ft.GridView(
                expand=1,
                child_aspect_ratio=1.0,
                runs_count=2,
                spacing=1,
                run_spacing=1,
            )
        )

        # Contenedor principal que contiene todos los elementos de la interfaz
        self.controls = [
            ft.Container(
                ft.Column([
                    self.imagenRecambios,
                    self.input_buscarRecambio,
                    self.BotonBuscarRecambio,
                    self.vistaResultadosBusqueda,
                    self.barraNavegacion,

                ]
                ),

                # propiedades contenedor principal
                border_radius=25,
                width=350,  # ancho
                height=655,  # Alto
                gradient=ft.LinearGradient([  # color del contenedor configurable en 2 tonos de color
                    "#FAFAF3",
                    "#FAFAF3",
                ])

            )
        ]


class VentanaIngreso(ft.View):
    '''Clase VentanaIngreso: Interfaz para ventana de ingresos.

    Args:
        - page: Instancia de la pagina actual.

    Contiene:
        - Imagen de diagnostico de ingresos como titulo.
        - Input para ingresar busqueda.
        - Boton ElevatedButton: para activar la busqueda.
        - Boton ElevatedButton: para añadir ingreso nuevo.
        - Boton ElevatedButton: para modificar ingreso.
        - Boton ElevatedButton: para eliminar ingreso.
        '''

    def __init__(self, page: ft.Page):
        '''Constructor de la interfaz grafica para la ventana Ingresos'''
        super(VentanaIngreso, self).__init__(
            route="/ingresos", horizontal_alignment=CrossAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER
        )

        self.page = page

        # Color de fondo contenedor principal
        self.bgcolor = "#FAFAF3"

        # Titulo imagen ingresos
        self.imagenVehiculos = ft.Container(
            ft.Container(
                bgcolor="#f6f6f6",
                width=320,
                height=90,
                padding=0,
                image_repeat=ImageRepeat.NO_REPEAT,
                shape=ft.BoxShape("rectangle"),
                # Define imagen
                image_src="/Imagen_de_Ingresos.png",
                image_fit=ft.ImageFit.COVER,
            ),
            alignment=ft.alignment.Alignment(x=0, y=0)
        )

        # Campo de entrada para la busqueda
        self.input_buscar = ft.TextField(
            label="Buscar Ingresos...",
            label_style=TextStyle(color='#6a6965', size=12),
            value="",
            border_radius=ft.border_radius.vertical(top=0, bottom=0),
            hint_text="Introduce la matricula del vehiculo",
            hint_style=TextStyle(color='#6a6965', size=10),
            color='black',
            height=40,
            cursor_color="#12597b",
            text_size=13,
            border_color="#12597b",
            autofocus=True,
            bgcolor="#E1F5FE"
        )

        # Boton de buscar cliente
        self.BotonBuscarVehiculo = ft.Container(
            ft.ElevatedButton(
                text="Buscar",
                color="white",
                bgcolor="#12597b",
                # icon=icons.LOGIN,
                # icon_color="333333",
                width=180,
                height=50,
                on_click=lambda _: page.go("/inicio")
            ),
            alignment=ft.alignment.Alignment(x=0, y=1)
        )

        # Barra de navegacion
        self.barraNavegacion = ft.NavigationBar(
            selected_index=0,
            # on_change=lambda e: self.on_navigation_change(e),
            destinations=[
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.HOME_OUTLINED,
                        color=ft.colors.GREY_900,
                        size=20  # Ajusta el tamaño del ícono no seleccionado
                    ),
                    selected_icon_content=ft.Icon(
                        name=ft.icons.HOME_ROUNDED,
                        color="#12597b",
                        size=24  # Ajusta el tamaño del ícono seleccionado
                    ),
                    label="Inicio",
                ),
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.PERSON_OUTLINED,
                        color=ft.colors.BLUE_GREY_900,
                        size=20
                    ),
                    selected_icon_content=ft.Icon(
                        name=ft.icons.PERSON,
                        color="#12597b",
                        size=24
                    ),
                    label="Cliente",

                ),
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.DIRECTIONS_CAR_OUTLINED,
                        color=ft.colors.BLUE_GREY_900,
                        size=20
                    ),
                    selected_icon_content=ft.Icon(
                        name=ft.icons.DIRECTIONS_CAR,
                        color="#12597b",
                        size=24
                    ),
                    label="Vehículo",
                ),
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.SETTINGS_OUTLINED,
                        color=ft.colors.BLUE_GREY_900,
                        size=20
                    ),
                    selected_icon_content=ft.Icon(
                        name=ft.icons.SETTINGS,
                        color="#12597b",
                        size=24
                    ),
                    label="Recambio",
                ),
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.CAR_REPAIR_OUTLINED,
                        color=ft.colors.BLUE_GREY_900,
                        size=20
                    ),
                    selected_icon_content=ft.Icon(
                        name=ft.icons.CAR_REPAIR,
                        color="#12597b",
                        size=24
                    ),
                    label="Ingreso",
                )
            ],
            bgcolor=ft.colors.GREY_400,  # Color de fondo de la barra de navegación (azul oscuro)
            indicator_color=ft.colors.AMBER_500,  # Color del indicador del destino seleccionado (ámbar)
            surface_tint_color=ft.colors.BLUE_GREY_900,  # Color de superficie para el material (cyan claro)
            label_behavior=ft.NavigationBarLabelBehavior.ONLY_SHOW_SELECTED  # Mostrar la etiqueta  seleccionada
        )

        # Contenedor para mostrar los resultados de busqueda
        self.vistaResultadosBusqueda = ft.Container(
            bgcolor='#FAFAF3',
            expand=True,
            content=ft.GridView(
                expand=1,
                child_aspect_ratio=1.0,
                runs_count=2,
                spacing=1,
                run_spacing=1,
            )
        )

        # Contenedor principal que contiene todos los elementos de la interfaz
        self.controls = [
            ft.Container(
                ft.Column([
                    self.imagenVehiculos,
                    self.input_buscar,
                    self.BotonBuscarVehiculo,
                    self.vistaResultadosBusqueda,
                    self.barraNavegacion,
                ]
                ),

                # propiedades contenedor principal
                border_radius=25,
                width=350,  # ancho
                height=655,  # Alto
                gradient=ft.LinearGradient([  # color del contenedor configurable en 2 tonos de color
                    "#FAFAF3",
                    "#FAFAF3",
                ])

            )
        ]


def main(page: ft.page):
    # configuración relacionada con la página
    page.title = "app"
    page.window.width = 350  # ancho de la pantalla
    page.vertical_alignment = "center"  # centramos verticalmente el container
    page.horizontal_alignment = "center"  # centramos horizontalmente el container

    # Metodo para manejar el enrutamiento de paginas
    def router(route):
        page.views.clear()

        if page.route == "/inicio":
            inicio = VentanaInicio(page)
            page.views.append(inicio)
        elif page.route == "/clientes":
            clientes = VentanaCliente(page)
            page.views.append(clientes)
        elif page.route == "/vehiculos":
            vehiculos = VentanaVehiculo(page)
            page.views.append(vehiculos)
        elif page.route == "/recambios":
            recambios = VentanaRecambios(page)
            page.views.append(recambios)
        elif page.route == "/ingresos":
            ingresos = VentanaIngreso(page)
            page.views.append(ingresos)

        page.update()

    page.on_route_change = router
    page.go("/inicio")
    # page.go("/clientes")
    # page.go("/vehiculos")
    # page.go("/recambios")
    # page.go("/ingresos")


# instanciar y ejecutar la aplicación
ft.app(target=main, assets_dir="assets")

