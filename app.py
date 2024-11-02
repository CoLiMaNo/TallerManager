from datetime import datetime
import flet as ft
from flet import *
from sqlalchemy import and_, desc, asc, or_
from sqlalchemy.exc import SQLAlchemyError
from models import Cliente, Vehiculo, Recambio, Ingreso, Registro
import db
import os
import json


class VentanaInicio(ft.View):
    '''Clase VentanaInicio: Interfaz gráfica de la ventana de inicio del sistema de gestión del taller.

    Esta clase representa la ventana principal de la aplicación, donde se muestran diversas opciones
    relacionadas con el análisis y reporte de datos del taller mecánico. En esta interfaz, el usuario
    puede acceder a diferentes funcionalidades clave para gestionar y analizar los datos de los clientes
    y el desempeño del taller.

    Args:
        - page: Instancia de la página actual, que maneja el contenido y las interacciones de la ventana.

    Contiene:
        - Botón ElevatedButton "Análisis de Costos por Cliente": Accede a una vista detallada que muestra el
          desglose de costos por cada cliente registrado en el sistema.
        - Botón ElevatedButton "Reporte de Beneficios": Permite al usuario consultar los beneficios generados
          por el taller, calculando la diferencia entre ingresos y costos.
        - Botón ElevatedButton "Estadísticas del Taller": Muestra un resumen del desempeño del taller,
          incluyendo la cantidad de vehículos atendidos y los tipos de reparaciones más comunes.
        - Botón ElevatedButton "Proyecciones Futuras": Accede a una vista de proyecciones basadas en datos
          históricos, como ingresos estimados o número de servicios futuros.
    '''


    def __init__(self, page: ft.Page):
        '''Constructor de la interfaz grafica para la ventana Inicio'''
        super(VentanaInicio, self).__init__(
            route="/inicio", horizontal_alignment=CrossAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER
        )

        self.page = page

        # Color de fondo contenedor principal
        self.bgcolor = "#ede0cc"

        # Logo de la App
        self.logo = ft.Container(
            ft.Container(
                bgcolor="#ede0cc",
                width=250,
                height=180,
                padding=0,
                image_repeat=ImageRepeat.NO_REPEAT,
                shape=ft.BoxShape("rectangle"),
                # Define imagen
                image_src="/logo-taller.png",
                image_fit=ft.ImageFit.COVER,
            ),
            alignment=ft.alignment.Alignment(x=0, y=0)
        )

        # Imagen vehiculo
        self.ImagenVehiculo = ft.Container(

            ft.Container(
                bgcolor="#ede0cc",
                width=200,
                height=90,
                padding=0,
                image_repeat=ImageRepeat.NO_REPEAT,
                shape=ft.BoxShape("rectangle"),
                # Define imagen
                image_src="/ImagenVehiculo2.png",
                image_fit=ft.ImageFit.COVER,
            ),
            expand=False,
            alignment=ft.alignment.Alignment(x=0, y=0)
        )

        # Boton para acceder al análisis de costos por cliente.
        self.boton_CostoPorCliente = ft.Container(
            ft.ElevatedButton(
                text="Costos por Cliente",
                color="white",
                bgcolor="#12597b",
                # icon=icons.LOGIN,
                # icon_color="333333",
                width=200,
                height=30,
                on_click=lambda _: page.go("/clientes")
            ),
            alignment=ft.alignment.Alignment(x=0, y=0)
        )

        # Boton para acceder a consultar los beneficios del taller.
        self.boton_ReporteBeneficios = ft.Container(
            ft.ElevatedButton(
                text="Reporte de Beneficios",
                color="white",
                bgcolor="#12597b",
                # icon=icons.LOGIN,
                # icon_color="333333",
                width=200,
                height=30,
                on_click=lambda _: page.go("/vehiculos")

            ),
            alignment=ft.alignment.Alignment(x=0, y=0)
        )

        # Boton para acceder al analisis del uso y desempeño general del taller
        self.boton_EstadisticasTaller = ft.Container(
            ft.ElevatedButton(
                text="Estadísticas del Taller",
                color="white",
                bgcolor="#12597b",
                # icon=icons.LOGIN,
                # icon_color="333333",
                width=200,
                height=30,
                on_click=lambda _: page.go("/recambios")
            ),
            alignment=ft.alignment.Alignment(x=0, y=0)
        )

        # Boton para acceder a proyecciones y análisis futuros
        self.boton_Proyecciones = ft.Container(
            ft.ElevatedButton(
                text="Proyecciones",
                color="white",
                bgcolor="#12597b",
                # icon=icons.LOGIN,
                # icon_color="333333",
                width=200,
                height=30,
                on_click=lambda _: page.go("/ingresos")
            ),
            alignment=ft.alignment.Alignment(x=0, y=0)
        )

        # contenedor vacio para relleno
        self.contenedor_vacio = ft.Container(
            expand= True
        )

        # Barra de navegacion VentanaInicio
        self.barraNavegacion = ft.NavigationBar(
            selected_index=0,
            height=50,
            on_change=lambda e: self.barra_de_navegacion(e),
            destinations=[
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.HOME_OUTLINED,
                        color="#12597b",
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
                        color="#12597b",
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
                        color="#12597b",
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
                        color="#12597b",
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
                        color="#12597b",
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
            bgcolor="#ede0cc",  # Color de fondo de la barra de navegación (azul oscuro)
            indicator_color=ft.colors.AMBER_500,  # Color del indicador del destino seleccionado (ámbar)
            surface_tint_color="#ede0cc",  # Color de superficie para el material (#ede0cc)
            label_behavior=ft.NavigationBarLabelBehavior.ONLY_SHOW_SELECTED  # Mostrar la etiqueta  seleccionada
        )

        # Contenedor principal que contiene todos los elementos de la interfaz
        self.controls = [
            ft.Container(
                ft.Column([
                    ft.Divider(height=10, color="transparent"),
                    self.logo,
                    ft.Divider(height=25, color="transparent"),
                    self.ImagenVehiculo,
                    ft.Divider(height=5, color="transparent"),
                    self.boton_CostoPorCliente,
                    ft.Divider(height=5, color="transparent"),
                    self.boton_ReporteBeneficios,
                    ft.Divider(height=5, color="transparent"),
                    self.boton_EstadisticasTaller,
                    ft.Divider(height=5, color="transparent"),
                    self.boton_Proyecciones,
                    self.contenedor_vacio,
                    self.barraNavegacion,
                ]
                ),

                # propiedades contenedor principal
                border_radius=25,
                width=350,  # ancho
                height=655,  # Alto
                gradient=ft.LinearGradient([  # color del contenedor configurable en 2 tonos de color
                    "#ede0cc",
                    "#ede0cc",
                ])

            )
        ]

    # metodo para navegar entre ventanas
    def barra_de_navegacion(self, e):
        selected_index = e.control.selected_index
        self.page.controls.clear()
        if selected_index == 0:
            self.page.go("/inicio")
        elif selected_index == 1:
            self.page.go("/clientes")
        elif selected_index == 2:
            self.page.go("/vehiculos")
        elif selected_index == 3:
            self.page.go("/recambios")
        elif selected_index == 4:
            self.page.go("/ingresos")
        self.page.update()


class VentanaCliente(ft.View):
    '''Clase VentanaClientes: Interfaz gráfica para la gestión de clientes.

    Esta clase representa la ventana de la aplicación dedicada a la gestión de clientes, donde el
    usuario puede realizar varias operaciones como búsqueda, adición, modificación y eliminación
    de clientes registrados en el sistema del taller.

    Args:
        - page: Instancia de la página actual, que maneja el contenido y las interacciones de la ventana.

    Contiene:
        - Imagen de título: Muestra una imagen de "Clientes" para identificar visualmente la sección.
        - Input: Campo de texto para ingresar el nombre del cliente a buscar.
        - Botón ElevatedButton "Buscar Cliente": Activa la búsqueda de clientes según los datos ingresados
          en el campo de búsqueda.
        - Botón ElevatedButton "Añadir Cliente": Permite al usuario añadir un nuevo cliente al sistema
          ingresando los datos requeridos (nombre, teléfono, dirección, etc.).
        - Botón ElevatedButton "Editar": Accede a una interfaz para editar los datos de un
          cliente existente en el sistema.
        - Botón ElevatedButton "Eliminar Cliente": Elimina del sistema los registros del cliente y el cliente seleccionado.
    '''


    def __init__(self, page: ft.Page):
        '''Constructor de la interfaz grafica para la ventana Clientes'''
        super(VentanaCliente, self).__init__(
            route="/clientes", horizontal_alignment=CrossAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER
        )

        self.page = page

        # Color de fondo contenedor principal
        self.bgcolor = "#ede0cc"

        # Imagen clientes
        self.imagenClientes = ft.Container(
            ft.Container(
                bgcolor="#ede0cc",
                width=320,
                height=70,
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
            height=35,
            cursor_color="#12597b",
            text_size=13,
            border_color="#12597b",
            autofocus=True,
            bgcolor="#E1F5FE"
        )

        # Boton para activar la busqueda cliente y boton agregar nuevo cliente
        self.BotonBuscarCliente = ft.Container(
            alignment=ft.alignment.Alignment(x=0, y=0),
            content=Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    # Boton buscar cliente
                    ft.ElevatedButton(
                        text="Buscar Cliente",
                        color="#FAFAF3",
                        bgcolor="#12597b",
                        tooltip='Buscar Cliente',
                        icon=icons.SEARCH,
                        icon_color="#FAFAF3",
                        width=180,
                        height=30,
                        on_click=lambda e: self.buscar_cliente(e),
                    ),
                    # Boton añadir nuevo
                    ft.IconButton(
                        icon=ft.icons.PERSON_ADD,
                        icon_color="#12597b",
                        icon_size=30,
                        tooltip="Añadir Nuevo",
                        on_click=lambda e: page.go("/clienteNuevo"),
                        )
                ]
            )
        )

        # Contenedor para mostrar los resultados de búsqueda
        self.vistaResultadosBusqueda = ft.Container(
            bgcolor='#ede0cc',
            expand=True,
            content=ft.GridView(
                expand=1,
                child_aspect_ratio=1.9, # ajusta la relacion alto por ancho
                runs_count=1,  # ajusta el número de columnas según el diseño
                spacing=1,  # Espacio entre las imágenes
                run_spacing=1,  # Espacio entre las filas
            )
        )

        # Barra de navegacion
        self.barraNavegacion = ft.NavigationBar(
            selected_index=1,
            height=50,
            on_change=lambda e: self.barra_de_navegacion(e),
            destinations=[
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.HOME_OUTLINED,
                        color="#12597b",
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
                        color="#12597b",
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
                        color="#12597b",
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
                        color="#12597b",
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
                        color="#12597b",
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
            bgcolor="#ede0cc",  # Color de fondo de la barra de navegación (azul oscuro)
            indicator_color=ft.colors.AMBER_500,  # Color del indicador del destino seleccionado (ámbar)
            surface_tint_color="#ede0cc",  # Color de superficie para el material (#ede0cc)
            label_behavior=ft.NavigationBarLabelBehavior.ONLY_SHOW_SELECTED  # Mostrar la etiqueta  seleccionada
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
                    "#ede0cc",
                    "#ede0cc",
                ])

            )
        ]

    # metodo para cargar los clientes existentes en el GridView
    def buscar_cliente(self,e):
        # Limpia los controles actuales del GridView
        self.vistaResultadosBusqueda.content.controls = []

        # input donde el usuario ingresa el nombre del cliente que quiere buscar
        nombre_cliente = self.input_buscar.value  # este es el Input

        # Buscamos el cliente por nombre (ignorando mayúsculas y minusculas)
        cliente_localizado = db.session.query(Cliente).filter(
            Cliente.nombre.ilike(f'%{nombre_cliente}%')).all()

        self.input_buscar.value = ""
        self.input_buscar.update()

        if cliente_localizado:
            cards = []
            for cliente in cliente_localizado:
                # mostramos detalles del cliente encontrado
                print(f"Nombre: {cliente.nombre}, Desde: {cliente.fecha_alta.strftime('%d/%m/%Y')}")
                card = ft.Card(
                    content=ft.Container(
                        alignment=ft.alignment.Alignment(x=0, y=0),
                        bgcolor="#4b8ca8",
                        padding=5,
                        border=ft.border.all(1, ft.colors.BLUE_800),
                        border_radius=ft.border_radius.all(10),
                        content=ft.Column([
                            ft.Container(
                                ft.Row(
                                    [
                                        ft.Text(f"{cliente.nombre}, ", size=12, weight=ft.FontWeight.W_700, text_align=ft.TextAlign.CENTER, no_wrap = False), # no_wrap Asegura que el texto se ajuste si es largo
                                        ft.Text(f"Desde: {cliente.fecha_alta.strftime('%d/%m/%Y')}", size=10, text_align=ft.TextAlign.LEFT)
                                    ],
                                    wrap=True,  # asegura que el contenido se ajuste en varias filas si es necesario
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                bgcolor="transparent",
                                alignment=ft.alignment.center
                            ),
                            ft.Container(
                                ft.Row(
                                    [
                                        ft.Text(f"Telefono:", size=10, weight=ft.FontWeight.W_700,text_align=ft.TextAlign.LEFT),
                                        ft.Text(f"{cliente.telefono}",size=10, text_align=ft.TextAlign.LEFT),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                bgcolor="transparent",
                                padding=0,
                                alignment=ft.alignment.center_left,

                            ),
                            ft.Container(
                                ft.Row(
                                    [
                                        ft.Text(f"Dirección:", size=10, weight=ft.FontWeight.W_700, text_align=ft.TextAlign.LEFT),
                                        ft.Text(f"{cliente.direccion}",size=10, text_align=ft.TextAlign.LEFT, no_wrap = False) # no_wrap Asegura que el texto se ajuste si es largo
                                    ],
                                    wrap=True,  # asegura que el contenido se ajuste en varias filas si es necesario
                                    alignment=ft.MainAxisAlignment.START,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                expand=True,
                                bgcolor="transparent",
                                padding=0,
                                alignment=ft.alignment.center_left,
                            ),
                            ft.Container(
                                ft.Row(
                                    [
                                        ft.Text(f"Correo:", size=10, weight=ft.FontWeight.W_700,
                                                text_align=ft.TextAlign.LEFT),
                                        ft.Text(f"{cliente.correo}", size=10, text_align=ft.TextAlign.LEFT, no_wrap = False) # no_wrap Asegura que el texto se ajuste si es largo
                                    ],
                                    wrap=True,  # asegura que el contenido se ajuste en varias filas si es necesario
                                    alignment=ft.MainAxisAlignment.START,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                bgcolor="transparent",
                                padding=0,
                                alignment=ft.alignment.center_left,
                            ),
                            #ft.Text(f"Vehiculos: {cliente.vehiculos}"),
                            ft.Row(
                                [
                                    ft.IconButton(
                                        icon=ft.icons.CAR_RENTAL,
                                        icon_color="#FAFAF3",
                                        icon_size=25,
                                        tooltip="Ingresos",
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.DIRECTIONS_CAR,
                                        icon_color="#FAFAF3",
                                        icon_size=25,
                                        tooltip="Vehiculos",
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.EDIT_NOTE,
                                        icon_color="#FAFAF3",
                                        icon_size=25,
                                        tooltip="Editar",
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.DELETE_FOREVER_ROUNDED,
                                        icon_color="red",
                                        icon_size=25,
                                        tooltip="Eliminar",
                                    ),
                                ],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                            vertical_alignment=ft.CrossAxisAlignment.END,
                            )
                        ])
                    )
                )

                cards.append(card)

            # agregar cards al GridView
            for card in cards:
                self.vistaResultadosBusqueda.content.controls.append(card)
            #actualizar la interfaz
            self.vistaResultadosBusqueda.update()

    def modificar_cliente(self):
        pass

    # metodo para navegar entre ventanas
    def barra_de_navegacion(self, e):
        selected_index = e.control.selected_index
        if selected_index == 0:
            self.page.go("/inicio")
        elif selected_index == 1:
            self.page.go("/clientes")
        elif selected_index == 2:
            self.page.go("/vehiculos")
        elif selected_index == 3:
            self.page.go("/recambios")
        elif selected_index == 4:
            self.page.go("/ingresos")

class VentanaClienteNuevo(ft.View):
    '''Clase VentanaNuevoCliente: Interfaz gráfica para la gestión de clientes.

    Esta clase representa la ventana de la aplicación dedicada a la adición de clientes nuevos en el sistema
    del taller.

    Args:
        - page: Instancia de la página actual, que maneja el contenido y las interacciones de la ventana.

    Contiene:
        - Imagen de título: Muestra una imagen de "Gestión de clientes" para identificar visualmente la sección.
        - Input: Campo de texto para ingresar el nombre del cliente.
        - Input: Campo de texto para ingresar el telefono del cliente.
        - Input: Campo de texto para ingresar el correo electronico del cliente.
        - Input: Campo de texto para ingresar el domicilio del cliente.
        - Botón ElevatedButton: "Aceptar" activa la accion de añadir el cliente al sistema los registros del taller
        - Botón ElevatedButton: "Cancelar" cancela la operacion de añadir el cliente.
    '''

    def __init__(self, page: ft.Page):
        '''Constructor de la interfaz grafica para la ventana Cliente Nuevo'''
        super(VentanaClienteNuevo, self).__init__(
            route="/clienteNuevo", horizontal_alignment=CrossAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER
        )

        self.page = page

        # Color de fondo contenedor principal
        self.bgcolor = "#ede0cc"

        # Imagen gestion de cliente
        self.imagen_gestionCliente = ft.Container(
            ft.Container(
                bgcolor="#ede0cc",
                width=320,
                height=120,
                padding=0,
                image_repeat=ImageRepeat.NO_REPEAT,
                shape=ft.BoxShape("rectangle"),
                # Define imagen
                image_src="/ImagenClienteNuevo.png",
                image_fit=ft.ImageFit.COVER,
            ),
            alignment=ft.alignment.Alignment(x=0, y=0)
        )

        # Campo de entrada para el nombre del cliente
        self.input_nombreCliente = ft.TextField(
            label="Nombre",
            label_style=TextStyle(color='#12597b', size=12),
            value="",
            border_radius=ft.border_radius.vertical(top=0, bottom=0),
            hint_text="Introduce el nombre del cliente",
            hint_style=TextStyle(color='#6a6965', size=10),
            color='black',
            height=35,
            cursor_color="#12597b",
            text_size=13,
            border_color="transparent",
            autofocus=True,
            bgcolor="#E1F5FE"
        )

        # Campo de entrada para el telefono del cliente
        self.input_telefonoCliente = ft.TextField(
            label="Telefono",
            label_style=TextStyle(color='#12597b', size=12),
            value="",
            border_radius=ft.border_radius.vertical(top=0, bottom=0),
            hint_text="Introduce el telefono del cliente",
            hint_style=TextStyle(color='#6a6965', size=10),
            color='black',
            height=35,
            cursor_color="#12597b",
            text_size=13,
            border_color="transparent",
            autofocus=True,
            bgcolor="#E1F5FE"
        )

        # Campo de entrada para el correo electronico del cliente
        self.input_correoCliente = ft.TextField(
            label="Correo Electronico",
            label_style=TextStyle(color='#12597b', size=12),
            value="",
            border_radius=ft.border_radius.vertical(top=0, bottom=0),
            hint_text="Introduce el correo del cliente",
            hint_style=TextStyle(color='#6a6965', size=10),
            color='black',
            height=35,
            cursor_color="#12597b",
            text_size=13,
            border_color="transparent",
            autofocus=True,
            bgcolor="#E1F5FE"
        )

        # Campo de entrada para la direccion del cliente
        self.input_direccionCliente = ft.Container(
            bgcolor='#E1F5FE',
            # border=ft.border.all(ft.colors.ORANGE_100),
            # expand=True,
            height=180,
            content=
            ft.TextField(
                filled=False,
                label="Direccion",
                label_style=TextStyle(color='#12597b', size=12, ),
                expand=True,
                value="",
                border_radius=ft.border_radius.vertical(top=5, bottom=5),
                hint_text="Introduce la direccion del cliente",
                hint_style=TextStyle(color='#6a6965', size=10),
                max_length=200,  # maximo de caracteres que se pueden ingresar en TextField
                # max_lines =  10, # maximo de líneas que se mostraran a la vez
                multiline=True,  # puede contener varias lineas de texto
                color='black',
                height=180,
                cursor_color="#12597b",
                text_size=13,
                border_color="transparent",
                autofocus=False,
                bgcolor="#E1F5FE",
                text_vertical_align=ft.VerticalAlignment.START,
            )
        )

        # Botones para agregar y cancelar operacion
        self.BotonAgregarCliente = ft.Container(
            expand=True,
            alignment=ft.alignment.Alignment(x=0, y=0),
            content=Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    # Boton agregar cliente nuevo
                    ft.ElevatedButton(
                        text="Aceptar",
                        color="#FAFAF3",
                        bgcolor="#12597b",
                        tooltip='Aceptar Añadir',
                        icon=icons.ADD,
                        icon_color="#FAFAF3",
                        width=140,
                        height=30,
                        on_click=lambda e: (self.cliente_nuevo(e), page.go("/clientes")),
                    ),
                    # cancelar operacion
                    ft.ElevatedButton(
                        text="Cancelar",
                        color="#FAFAF3",
                        bgcolor="#12597b",
                        tooltip='Cancelar Añadir',
                        icon=icons.CANCEL,
                        icon_color="#FAFAF3",
                        width=140,
                        height=30,
                        on_click=lambda _: page.go("/clientes"),
                    ),
                ]
            )
        )

        # Contenedor principal que contiene todos los elementos de la interfaz
        self.controls = [
            ft.Container(
                ft.Column([
                    # self.tituloClientes,
                    self.imagen_gestionCliente,
                    self.input_nombreCliente,
                    self.input_telefonoCliente,
                    self.input_correoCliente,
                    self.input_direccionCliente,
                    self.BotonAgregarCliente,
                ]
                ),

                # propiedades contenedor principal
                border_radius=25,
                width=350,  # ancho
                height=655,  # Alto
                gradient=ft.LinearGradient([  # color del contenedor configurable en 2 tonos de color
                    "#ede0cc",
                    "#ede0cc",
                ])

            )
        ]

    # metodo para añadir un nuevo cliente al sistema del taller
    def cliente_nuevo(self, e):
        print("\n > Crear cliente")
        # Captura y limpieza de los datos ingresados por el usuario
        nombre = self.input_nombreCliente.value.strip()  # Nombre del cliente
        telefono = self.input_telefonoCliente.value.strip() # Teléfono de contacto del cliente
        correo = self.input_correoCliente.value.strip() # Correo electrónico del cliente
        direccion = self.input_direccionCliente.content.value.strip() # Dirección del cliente
        fecha_alta = datetime.now() # Fecha de registro del cliente en el sistema

        # Creación de una nueva instancia de Cliente con los datos proporcionados
        nuevo_cliente = Cliente(nombre=nombre, telefono=telefono, direccion=direccion, correo=correo,
                                fecha_alta=fecha_alta)

        # Agregar el nuevo cliente a la sesión de la base de datos
        db.session.add(nuevo_cliente)

        # Guardar los cambios en la base de datos y cerrar la sesión
        db.session.commit()
        db.session.close()


class VentanaVehiculo(ft.View):
    '''Clase VentanaVehiculo: Interfaz gráfica para la gestión de vehículos.

    Esta clase representa la ventana de la aplicación dedicada a la gestión de vehículos, donde el
    usuario puede realizar operaciones como búsqueda, adición, modificación y eliminación de los vehículos
    registrados en el sistema del taller.

    Args:
        - page: Instancia de la página actual, que maneja el contenido y las interacciones de la ventana.

    Contiene:
        - Imagen de título: Muestra una imagen de "Vehículos" para identificar visualmente la sección.
        - Input: Campo de texto para ingresar la matrícula o los datos del vehículo a buscar.
        - Botón ElevatedButton "Buscar Vehículo": Activa la búsqueda de vehículos en base a los datos ingresados.
        - Botón ElevatedButton "Añadir Vehículo": Permite al usuario añadir un nuevo vehículo al sistema
          ingresando los datos requeridos (marca, modelo, matrícula, kilometraje, etc.).
        - Botón ElevatedButton "Modificar Vehículo": Accede a una interfaz para modificar los datos de un
          vehículo existente en el sistema.
        - Botón ElevatedButton "Eliminar Vehículo": Elimina del sistema los registros del vehículo seleccionado.
    '''


    def __init__(self, page: ft.Page):
        '''Constructor de la interfaz grafica para la ventana Vehiculos'''
        super(VentanaVehiculo, self).__init__(
            route="/vehiculos", horizontal_alignment=CrossAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER
        )

        self.page = page

        # Color de fondo contenedor principal
        self.bgcolor = "#ede0cc"

        # Titulo con imagen vehiculo
        self.imagenVehiculos = ft.Container(
            ft.Container(
                bgcolor="#ede0cc",
                width=320,
                height=70,
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
            height=35,
            cursor_color="#12597b",
            text_size=13,
            border_color="#12597b",
            autofocus=True,
            bgcolor="#E1F5FE"
        )

        # Boton para activar la busqueda del vehiculo y boton agregar nuevo vehiculo
        self.BotonBuscarVehiculo = ft.Container(
            alignment=ft.alignment.Alignment(x=0, y=0),
            content=Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    # Boton buscar cliente y añadir nuevo
                    ft.ElevatedButton(
                        text="Buscar Vehiculo",
                        color="#FAFAF3",
                        bgcolor="#12597b",
                        tooltip='Buscar Vehiculo',
                        icon=icons.SEARCH,
                        icon_color="#FAFAF3",
                        width=180,
                        height=30,
                        on_click=lambda e: self.buscar_vehiculo(e),
                    ),
                    ft.IconButton(
                        content=ft.Image(src="car-add.png",
                                         color= "#12597b",
                                         height=30,
                                         width=30),
                        tooltip="Añadir Nuevo",
                        on_click=lambda e: page.go("/vehiculoNuevo"),
                    )
                ]
            )
        )
        # Contenedor para mostrar los resultados de búsqueda
        self.vistaResultadosBusqueda = ft.Container(
            bgcolor='#ede0cc',
            expand=True,
            content=ft.GridView(
                expand=1,
                child_aspect_ratio=1.9, # ajusta la relacion alto por ancho
                runs_count=1,  # ajusta el número de columnas según el diseño
                spacing=1,  # Espacio entre las imágenes
                run_spacing=1,  # Espacio entre las filas
            )
        )

        # Barra de navegacion
        self.barraNavegacion = ft.NavigationBar(
            selected_index=2,
            height=50,
            on_change=lambda e: self.barra_de_navegacion(e),
            destinations=[
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.HOME_OUTLINED,
                        color="#12597b",
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
                        color="#12597b",
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
                        color="#12597b",
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
                        color="#12597b",
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
                        color="#12597b",
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
            bgcolor="#ede0cc",  # Color de fondo de la barra de navegación (azul oscuro)
            indicator_color=ft.colors.AMBER_500,  # Color del indicador del destino seleccionado (ámbar)
            surface_tint_color="#ede0cc",  # Color de superficie para el material (#ede0cc)
            label_behavior=ft.NavigationBarLabelBehavior.ONLY_SHOW_SELECTED  # Mostrar la etiqueta  seleccionada
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
                    "#ede0cc",
                    "#ede0cc",
                ])

            )
        ]

        # metodo de navegacion para la barra de navegacion

    # metodo para cargar los vehiculos existentes en el GridView
    def buscar_vehiculo(self,e):
        # Limpia los controles actuales del GridView
        self.vistaResultadosBusqueda.content.controls = []

        # input donde el usuario ingresa el nombre del cliente que quiere buscar
        matricula_vehiculo = self.input_buscar.value  # este es el Input

        # Buscamos el vehiculo por matricula (ignorando mayúsculas y minusculas)
        vehiculo_localizado = db.session.query(Vehiculo).filter(
            Vehiculo.matricula.ilike(f'%{matricula_vehiculo}%')).all()

        self.input_buscar.value = ""
        self.input_buscar.update()

        if vehiculo_localizado:
            cards = []
            for vehiculo in vehiculo_localizado:
                # Obtenemos el cliente asociado al vehículo
                cliente = db.session.query(Cliente).filter_by(id_cliente=vehiculo.id_cliente).first()

                # Mostramos detalles del vehículo y del cliente encontrado
                if cliente:  # Verificamos si se encontró un cliente
                    print(f"Cliente: {cliente.nombre}, Vehículo: {vehiculo.matricula}, Desde: {vehiculo.fecha_alta.strftime('%d/%m/%Y')}")

                card = ft.Card(
                        content=ft.Container(
                            alignment=ft.alignment.Alignment(x=0, y=0),
                            bgcolor="#4b8ca8",
                            padding=5,
                            border=ft.border.all(1, ft.colors.BLUE_800),
                            border_radius=ft.border_radius.all(10),
                            content=ft.Column([
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.Text(f"{cliente.nombre}, ", size=12, weight=ft.FontWeight.W_700, text_align=ft.TextAlign.CENTER, no_wrap=False), # no_wrap Asegura que el texto se ajuste si es largo
                                            ft.Text(f"Desde: {vehiculo.fecha_alta.strftime('%d/%m/%Y')}", size=10, text_align=ft.TextAlign.LEFT)
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                    bgcolor="transparent",
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.Text(f"Desde:", size=10, weight=ft.FontWeight.W_700,text_align=ft.TextAlign.LEFT),
                                            ft.Text(f"{vehiculo.marca}",size=10, text_align=ft.TextAlign.LEFT),
                                        ],
                                        alignment=ft.MainAxisAlignment.START,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                    bgcolor="transparent",
                                    padding=0,
                                    alignment=ft.alignment.center_left,

                                ),
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.Text(f"Modelo:", size=10, weight=ft.FontWeight.W_700, text_align=ft.TextAlign.LEFT),
                                            ft.Text(f"{vehiculo.modelo}",size=10, text_align=ft.TextAlign.LEFT)
                                        ],
                                        alignment=ft.MainAxisAlignment.START,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                    bgcolor="transparent",
                                    padding=0,
                                    alignment=ft.alignment.center_left,
                                ),
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.Text(f"Matricula:", size=10, weight=ft.FontWeight.W_700,
                                                    text_align=ft.TextAlign.LEFT),
                                            ft.Text(f"{vehiculo.matricula}", size=10, text_align=ft.TextAlign.LEFT)
                                        ],
                                        alignment=ft.MainAxisAlignment.START,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                    bgcolor="transparent",
                                    padding=0,
                                    alignment=ft.alignment.center_left,
                                ),
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.Text(f"Kilometros:", size=10, weight=ft.FontWeight.W_700,
                                                    text_align=ft.TextAlign.LEFT),
                                            ft.Text(f"{vehiculo.kilometros}", size=10, text_align=ft.TextAlign.LEFT)
                                        ],
                                        alignment=ft.MainAxisAlignment.START,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                    bgcolor="transparent",
                                    padding=0,
                                    alignment=ft.alignment.center_left,
                                ),
                                ft.Row(
                                    [
                                        ft.ElevatedButton(
                                            bgcolor="#12597b",
                                            width=95,
                                            height=20,
                                            content= ft.Text("Ingresos", color="white", size=11,bgcolor="#12597b")), #on_click=lambda: editar_cliente(cliente)),
                                        ft.ElevatedButton(
                                            bgcolor="#12597b",
                                            width=80 ,
                                            height=20,
                                            content=ft.Text("Editar", color="white", size=11,bgcolor="#12597b"))
                                    ],
                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                vertical_alignment=ft.CrossAxisAlignment.END,
                                )
                            ])
                        )
                    )

                cards.append(card)

            # agregar cards al GridView
            for card in cards:
                self.vistaResultadosBusqueda.content.controls.append(card)
            #actualizar la interfaz
            self.vistaResultadosBusqueda.update()

    # metodo para navegar entre ventanas
    def barra_de_navegacion(self, e):
        selected_index = e.control.selected_index
        if selected_index == 0:
            self.page.go("/inicio")
        elif selected_index == 1:
            self.page.go("/clientes")
        elif selected_index == 2:
            self.page.go("/vehiculos")
        elif selected_index == 3:
            self.page.go("/recambios")
        elif selected_index == 4:
            self.page.go("/ingresos")


class VentanaVehiculoNuevo(ft.View):
    '''Clase VentanaVehiculoNuevo: Interfaz gráfica para la gestión de vehiculos.

    Esta clase representa la ventana de la aplicación dedicada a la adición de vehiculos nuevos en el sistema
    del taller.

    Args:
        - page: Instancia de la página actual, que maneja el contenido y las interacciones de la ventana.

    Contiene:
        - Imagen de título: Muestra una imagen de "Gestión de vehiculos" para identificar visualmente la sección.
        - Input: Campo de texto para ingresar la marca del vehiculo.
        - Input: Campo de texto para ingresar el el modelo del vehiculo
        - Input: Campo de texto para ingresar la matricula del vehiculo.
        - Input: Campo de texto para ingresar los kilometros del vehiculo.
        - Botón ElevatedButton: "Aceptar" activa la accion de añadir el vehiculo al sistema los registros del taller
        - Botón ElevatedButton: "Cancelar" cancela la operacion de añadir el vehiculo.
    '''

    def __init__(self, page: ft.Page):
        '''Constructor de la interfaz grafica para la ventana Vehiculo Nuevo'''
        super(VentanaVehiculoNuevo, self).__init__(
            route="/vehiculoNuevo", horizontal_alignment=CrossAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER
        )

        self.page = page

        # Color de fondo contenedor principal
        self.bgcolor = "#ede0cc"

        # Imagen gestion de vehiculos
        self.imagen_gestionVehiculo = ft.Container(
            ft.Container(
                bgcolor="#ede0cc",
                width=320,
                height=120,
                padding=0,
                image_repeat=ImageRepeat.NO_REPEAT,
                shape=ft.BoxShape("rectangle"),
                # Define imagen
                image_src="/imagen_de_nuevo_vehiculo.png",
                image_fit=ft.ImageFit.COVER,
            ),
            alignment=ft.alignment.Alignment(x=0, y=0)
        )

        # Objeto Text para mostrar la opción elegida
        self.texto_opcion_elegida = ft.Text()

        # menu desplegable para elegir el cliente del vehiculo
        self.menu_clientes = ft.Container(
            alignment=ft.alignment.Alignment(x=0, y=0),
            content=Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Dropdown(
                        label='Selecciona un Cliente',
                        alignment=Alignment(0.0, 0.0),
                        label_style=TextStyle(color='#12597b', size=12, bgcolor='#ede0cc', weight=ft.FontWeight.W_700),
                        options_fill_horizontally=True,
                        dense=True,
                        max_menu_height=True,
                        height=50,
                        width=300,
                        content_padding=6,
                        color='#12597b',
                        border_color='#12597b',
                        text_size=10,
                        on_change=lambda e: (self.pestaniaOpcion(e)),
                        options=[ft.dropdown.Option(str(cliente.nombre))
                            for cliente in db.session.query(Cliente).all()],
                        bgcolor="#ede0cc",
                        padding=0,
                    )
                ]
            )
        )

        # Campo de entrada para la marca del vehiculo
        self.input_marcaVehiculo = ft.TextField(
            label="Marca",
            label_style=TextStyle(color='#12597b', size=12),
            value="",
            border_radius=ft.border_radius.vertical(top=0, bottom=0),
            hint_text="Introduce la marca del vehiculo",
            hint_style=TextStyle(color='#6a6965', size=10),
            color='black',
            height=35,
            cursor_color="#12597b",
            text_size=13,
            border_color="transparent",
            autofocus=True,
            bgcolor="#E1F5FE"
        )

        # Campo de entrada para el modelo del vehiculo
        self.input_modeloVehiculo = ft.TextField(
            label="Modelo",
            label_style=TextStyle(color='#12597b', size=12),
            value="",
            border_radius=ft.border_radius.vertical(top=0, bottom=0),
            hint_text="Introduce el modelo del vehiculo",
            hint_style=TextStyle(color='#6a6965', size=10),
            color='black',
            height=35,
            cursor_color="#12597b",
            text_size=13,
            border_color="transparent",
            autofocus=True,
            bgcolor="#E1F5FE"
        )

        # Campo de entrada para la matricula del vehiculo
        self.input_matriculaVehiculo = ft.TextField(
            label="Matricula",
            label_style=TextStyle(color='#12597b', size=12),
            value="",
            border_radius=ft.border_radius.vertical(top=0, bottom=0),
            hint_text="Introduce la matricula del vehiculo",
            hint_style=TextStyle(color='#6a6965', size=10),
            color='black',
            height=35,
            cursor_color="#12597b",
            text_size=13,
            border_color="transparent",
            autofocus=True,
            bgcolor="#E1F5FE"
        )

        # Campo de entrada para los kilometros del vehiculo
        self.input_kilometrosVehiculo = ft.TextField(
            label="Kilometros",
            label_style=TextStyle(color='#12597b', size=12),
            value="",
            border_radius=ft.border_radius.vertical(top=0, bottom=0),
            hint_text="Introduce los kilometros del vehiculo",
            hint_style=TextStyle(color='#6a6965', size=10),
            color='black',
            height=35,
            cursor_color="#12597b",
            text_size=13,
            border_color="transparent",
            autofocus=True,
            bgcolor="#E1F5FE"
        )

        # Botones para agregar y cancelar operacion
        self.BotonAgregarCliente = ft.Container(
            expand=True,
            alignment=ft.alignment.Alignment(x=0, y=0),
            content=Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    # Boton agregar cliente nuevo
                    ft.ElevatedButton(
                        text="Aceptar",
                        color="#FAFAF3",
                        bgcolor="#12597b",
                        tooltip='Aceptar Añadir',
                        icon=icons.ADD,
                        icon_color="#FAFAF3",
                        width=140,
                        height=30,
                        on_click=lambda e: (self.vehiculo_nuevo(e), page.go("/vehiculos")),
                    ),
                    # cancelar operacion
                    ft.ElevatedButton(
                        text="Cancelar",
                        color="#FAFAF3",
                        bgcolor="#12597b",
                        tooltip='Cancelar Añadir',
                        icon=icons.CANCEL,
                        icon_color="#FAFAF3",
                        width=140,
                        height=30,
                        on_click=lambda _: page.go("/vehiculos"),
                    ),
                ]
            )
        )

        # Contenedor principal que contiene todos los elementos de la interfaz
        self.controls = [
            ft.Container(
                ft.Column([
                    # self.tituloClientes,
                    self.imagen_gestionVehiculo,
                    self.menu_clientes,
                    self.input_marcaVehiculo,
                    self.input_modeloVehiculo,
                    self.input_matriculaVehiculo,
                    self.input_kilometrosVehiculo,
                    self.BotonAgregarCliente,
                ]
                ),

                # propiedades contenedor principal
                border_radius=25,
                width=350,  # ancho
                height=655,  # Alto
                gradient=ft.LinearGradient([  # color del contenedor configurable en 2 tonos de color
                    "#ede0cc",
                    "#ede0cc",
                ])

            )
        ]

    # metodo para manejar la opcion seleccionada en el menu desplegable
    def pestaniaOpcion(self, e):
        # Obtener la opción seleccionada
        elegirOpcion = self.menu_clientes.content.controls[0].value

        # Actualizar texto con la opción elegida
        self.texto_opcion_elegida.value = (
            f"Opción elegida: {elegirOpcion}" if elegirOpcion else "No se ha seleccionado ninguna opción."
        )

        # Imprime la opción seleccionada
        print(f"Cliente seleccionado: {elegirOpcion}")

        # Actualiza la interfaz
        self.page.update(self)

    # metodo para añadir un nuevo vehículo al sistema del taller
    def vehiculo_nuevo(self, e):
        print("\n > Crear vehiculo")
        # Obtención de datos de entrada para el nuevo vehículo y cliente
        id_cliente = self.menu_clientes.content.controls[0].value.strip() # ID o nombre del cliente seleccionado
        marca = self.input_marcaVehiculo.value.strip()  # Marca del vehículo
        modelo = self.input_modeloVehiculo.value.strip() # Modelo del vehículo
        matricula = self.input_matriculaVehiculo.value.strip() # Matrícula del vehículo
        kilometros = self.input_kilometrosVehiculo.value.strip() # Kilómetros actuales del vehículo
        fecha_alta = datetime.now() # Fecha de alta del vehículo en el sistema

        # Consulta para encontrar el cliente en la base de datos por nombre (o ID según el valor seleccionado)
        cliente = db.session.query(Cliente).filter_by(nombre=id_cliente).first()

        # Creación de una nueva instancia de Vehiculo con los datos de entrada
        nuevo_vehiculo = Vehiculo(marca=marca, modelo=modelo, matricula=matricula, kilometros=kilometros, fecha_alta=fecha_alta)

        # Agregar el nuevo vehículo a la sesión de la base de datos
        db.session.add(nuevo_vehiculo)

        # Establecer la relación bidireccional entre el cliente y el vehículo
        # Se añade el vehículo a la lista de vehículos del cliente, gestionando la relación automáticamente
        cliente.vehiculos.append(nuevo_vehiculo)

        # Confirmar y cerrar la sesión
        db.session.commit()
        db.session.close()


class VentanaCrearRecambio(ft.View):
    '''Clase VentanaRecambios: Interfaz gráfica para la gestión de recambios.

      Esta clase representa la ventana de la aplicación dedicada a la gestión de recambios, donde el
      usuario puede realizar operaciones como búsqueda, adición, modificación y eliminación de recambios
      utilizados en las reparaciones.

      Args:
          - page: Instancia de la página actual, que maneja el contenido y las interacciones de la ventana.

      Contiene:
          - Imagen de título: Muestra una imagen de "Recambios" para identificar visualmente la sección.
          - Input: Campo de texto para ingresar el nombre o los detalles del recambio a buscar.
          - Botón ElevatedButton "Buscar Recambio": Activa la búsqueda de recambios en base a los datos ingresados.
          - Botón ElevatedButton "Añadir Recambio": Permite al usuario añadir un nuevo recambio al sistema ingresando
            los datos requeridos (nombre, descripción, costo, etc.).
          - Botón ElevatedButton "Modificar Recambio": Accede a una interfaz para modificar los datos de un
            recambio existente en el sistema.
          - Botón ElevatedButton "Eliminar Recambio": Elimina del sistema los registros del recambio seleccionado.
      '''

    def __init__(self, page: ft.Page):
        '''Constructor de la interfaz grafica para la ventana recambios'''
        super(VentanaCrearRecambio, self).__init__(
            route="/crearRecambio", horizontal_alignment=CrossAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER
        )

        # Ruta completa al archivo JSON del menu para los recambios
        self.ruta_json = r'C:\Users\Juan Carlos\espacio_de_trabajo\AAA Practicas personal\TallerManager\database\menu_recambios.json'

        self.page = page

        # Color de fondo contenedor principal
        self.bgcolor = "#ede0cc"

        # Titulo imagen recambios
        self.imagenRecambios = ft.Container(
            ft.Container(
                bgcolor="#ede0cc",
                width=320,
                height=100,
                padding=0,
                image_repeat=ImageRepeat.NO_REPEAT,
                shape=ft.BoxShape("rectangle"),
                # Define imagen
                image_src="/ImagenCrearRecambio.png",
                image_fit=ft.ImageFit.COVER,
            ),
            alignment=ft.alignment.Alignment(x=0, y=0)
        )

        # Campo de entrada para nombre del recambio
        self.input_nombreRecambio = ft.Container(
            bgcolor='#FAFAF3',
            # border=ft.border.all(ft.colors.ORANGE_100),
            #expand=True,
            height=70,
            content=
            ft.TextField(
                filled=False,
                label="Nombre del Recambio...",
                label_style=TextStyle(color='#12597b', size=12),
                value="",
                border_radius=ft.border_radius.vertical(top=5, bottom=5),
                hint_text="Introduce el Nombre",
                hint_style=TextStyle(color='#6a6965', size=10),
                max_length=70,  # maximo de caracteres que se pueden ingresar en TextField
                multiline=True,  # puede contener varias lineas de texto
                color='black',
                height=90,
                cursor_color="#12597b",
                text_size=13,
                border_color="transparent",
                autofocus=True,
                bgcolor="transparent",
            )
        )

        # Campo de entrada para la descripcion del recambio
        self.input_descripcionRecambio = ft.Container(
            bgcolor='#FAFAF3',
            # border=ft.border.all(ft.colors.ORANGE_100),
            #expand=True,
            height=180,
            content=
                ft.TextField(
                    filled=False,
                    label="Descripccion del Recambio...",
                    label_style=TextStyle(color='#12597b', size=12, ),
                    expand=True,
                    value="",
                    border_radius=ft.border_radius.vertical(top=5, bottom=5),
                    hint_text="Introduce la Descripcion",
                    hint_style=TextStyle(color='#6a6965', size=10),
                    max_length=180,  # maximo de caracteres que se pueden ingresar en TextField
                    # max_lines =  10, # maximo de líneas que se mostraran a la vez
                    multiline=True,  # puede contener varias lineas de texto
                    color='black',
                    height=180,
                    cursor_color="#12597b",
                    text_size=13,
                    border_color="transparent",
                    autofocus=False,
                    bgcolor="transparent",
                    text_vertical_align=ft.VerticalAlignment.START,
                )
            )

        # Menu desplegable principal para elegir una opcion
        self.categoria = ft.Container(
            alignment=ft.alignment.Alignment(x=0, y=0),
            content=Row(
                alignment=ft.MainAxisAlignment.START,
                controls=[
                    ft.Dropdown(
                        label='Selecciona Categoría',
                        alignment = Alignment(0.0, 0.0),
                        label_style=TextStyle(color='#12597b', size=13, bgcolor= '#ede0cc', weight=ft.FontWeight.W_700),
                        options_fill_horizontally =True,
                        dense = True,
                        height=40,
                        width=300,
                        content_padding=6,
                        color='#12597b',
                        border_color='#12597b',
                        text_size=11,
                        on_change=lambda e: (self.pestaniaOpcion(e),
                                             self.actualizar_submenu(e)),
                        options=[
                            # Lista de opciones para los recambios
                            ft.dropdown.Option("Accesorios para coche"),
                            ft.dropdown.Option("Aceites y líquidos"),
                            ft.dropdown.Option("Aire acondicionado"),
                            ft.dropdown.Option("Amortiguacion"),
                            ft.dropdown.Option("Árboles de transmisión y diferenciales"),
                            ft.dropdown.Option("Caja de cambios"),
                            ft.dropdown.Option("Calefacción y ventilación"),
                            ft.dropdown.Option("Carrocería"),
                            ft.dropdown.Option("Correas, cadenas, rodillos"),
                            ft.dropdown.Option("Direccion"),
                            ft.dropdown.Option("Embrague"),
                            ft.dropdown.Option("Encendido y precalentamiento"),
                            ft.dropdown.Option("Escape"),
                            ft.dropdown.Option("Filtros"),
                            ft.dropdown.Option("Frenos"),
                            ft.dropdown.Option("Herramientas y equipo"),
                            ft.dropdown.Option("Iluminación"),
                            ft.dropdown.Option("Interior"),
                            ft.dropdown.Option("Juntas y retenes"),
                            ft.dropdown.Option("Kit de reparación"),
                            ft.dropdown.Option("Motor"),
                            ft.dropdown.Option("Neumáticos"),
                            ft.dropdown.Option("Palier y junta homocinetica"),
                            ft.dropdown.Option("Productos para cuidado del coche"),
                            ft.dropdown.Option("Remolque / piezas adicionales"),
                            ft.dropdown.Option("Rodamientos"),
                            ft.dropdown.Option("Sensores, relés, unidades de control"),
                            ft.dropdown.Option("Sistema de combustible"),
                            ft.dropdown.Option("Sistema de refrigeración del motor"),
                            ft.dropdown.Option("Sistema electrico"),
                            ft.dropdown.Option("Sistema limpiaparabrisas"),
                            ft.dropdown.Option("Sujeciones"),
                            ft.dropdown.Option("Suspension"),
                            ft.dropdown.Option("Tuberías y mangueras"),
                            ft.dropdown.Option("Tuning")

                        ],
                        bgcolor="#ede0cc",
                        padding = 0,
                    )
                ]
            )
        )

        # Menu desplegable secundario para elegir una opcion
        self.subcategoria = ft.Dropdown(
                        label='Selecciona Subcategoría ',
                        alignment = Alignment(0.0, 0.0),
                        label_style=TextStyle(color='#12597b', size=13, bgcolor= '#ede0cc', weight=ft.FontWeight.W_700),
                        options_fill_horizontally =True,
                        dense = True,
                        max_menu_height=True,
                        height=50,
                        width=300,
                        content_padding=6,
                        color='#12597b',
                        border_color='#12597b',
                        text_size=10,
                        on_change=lambda e: (self.actualizar_submenu(e)),
                        options=[],
                        bgcolor="#ede0cc",
                        padding=0,
                    )

        # Boton para activar la creacion del recambio
        self.BotonCrearRecambio = ft.Container(
            expand=True,
            alignment=ft.alignment.Alignment(x=0, y=0),
            content=Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    # Boton buscar cliente y añadir nuevo
                    ft.ElevatedButton(
                        text="Aceptar",
                        color="#FAFAF3",
                        bgcolor="#12597b",
                        tooltip='Añadir Recambio',
                        icon=icons.ADD,
                        icon_color="#FAFAF3",
                        width=140,
                        height=30,
                        on_click=lambda e: (self.crear_recambio(e), page.go("/recambios")),
                    ), ft.ElevatedButton(
                        text="Cancelar",
                        color="#FAFAF3",
                        bgcolor="#12597b",
                        tooltip='Cancelar Ingreso',
                        icon=icons.CANCEL,
                        icon_color="#FAFAF3",
                        width=140,
                        height=30,
                        on_click=lambda _: page.go("/recambios"),
                    ),
                ]
            )
        )

        # Contenedor principal que contiene todos los elementos de la interfaz
        self.controls = [
            ft.Container(
                ft.Column([
                    self.imagenRecambios,
                    self.input_nombreRecambio,
                    self.input_descripcionRecambio,
                    self.categoria,
                    self.subcategoria,
                    self.BotonCrearRecambio,
                ]
                ),

                # propiedades contenedor principal
                border_radius=25,
                width=350,  # ancho
                height=655,  # Alto
                gradient=ft.LinearGradient([  # color del contenedor configurable en 2 tonos de color
                    "#ede0cc",
                    "#ede0cc",
                ])

            )
        ]


    # metodo para manejar la opcion seleccionada en el menu desplegable principal
    def pestaniaOpcion(self, e):

        # Crear un objeto Text para mostrar la opcion elegida
        t = ft.Text()

        # Obtener la opcion elegida del menu desplegable
        elegirOpcion = self.categoria.content.controls[0].value

        # Actualizar el valor del objeto Text con la opcion elegida
        t.value = f"Opción elegida: {elegirOpcion}"

        # Diccionario que mapea las opciones a las acciones correspondientes
        acciones = {
            'Neumaticos':'Añadir en Neumaticos',
            'Aceites y liquidos': 'Añadir en Aceites y liquidos',
            'Frenos': 'Añadir en Frenos',
            'Filtros': 'Añadir en Filtros',
            'Motor': 'Añadir en Motor',
            'Sistema limpiaparabrisas': 'Añadir en Sistema limpiparabrisas',
            'Encendido y precalentamiento': 'Añadir en Encendido y precalentamiento',
            'Suspension': 'Añadir en Suspension',
            'Sistema electrico': 'Añadir en Sistema electrico',
            'Amortiguacion': 'Añadir en Amortiguacion',
            'Correas,cadenas,rodillos': 'Añadir en Correas,cadenas,rodillos',
            'Sistema de refrigeracion del motor': 'Añadir en Sistema de refrigeracion del motor',
            'Carroceria': 'Añadir en Carroceria',
            'Calefaccion y ventilacion': 'Añadir en Calefaccion y ventilacion',
            'Juntas y retenes': 'Añadir en Juntas y retenes',
            'Escape': 'Añadir en Escape',
            'Interior': 'Añadir en Interior',
            'Sistema de combustible': 'Añadir en Sistema de combustible',
            'Direccion': 'Añadir en Direccion',
            'Embrague': 'Añadir en Embrague',
            'Palier y junta homocinetica': 'Añadir en Palier y junta homocinetica',
            'Remolque / piezas adicionales': 'Añadir en Remolque / piezas adicionales',
            'Caja de cambios': 'Añadir en Caja de cambios',
            'Aire acondicionado': 'Añadir en Aire acondicionado',
            'Rodamientos': 'Añadir en Rodamintos',
            'Arboles de transmision y diferenciales': 'Añadir en Arboles de transmision y diferenciales',
            'Sensores, reles, unidades de control': 'Añadir en Sensores, reles, unidades de control',
            'Accesorios para coche': 'Añadir en Accesorios para coche',
            'Kit de reparacion': 'Añadir en Kit de reparacion',
            'Herramientas y equipo': 'Añadir en Herramientas y equipo',
            'Tuberias y mangueras': 'Añadir en Tuberis y mangueras',
            'Productos para cuidado del coche': 'Añadir en Productos para cuidado del coche',
            'Iluminación': 'Añadir en Iluminación',
            'Tuning': 'Añadir en Tuning',
            'Sujeciones': 'Añadir en Sujeciones',
        }

        # Imprimir un mensaje segun la opcion elegida
        if elegirOpcion in acciones:
            print(acciones[elegirOpcion])
        else:
            print('Opcion no valida')

        # Actualizar la pagina con el objeto Text
        self.page.update(self)
        # Agregar el objeto Text a la pagina
        self.page.add(t)

        db.session.close()

    # metodo para cargar el menu de recambios en .json
    def cargar_menu_json(self, ruta_json):
        with open(ruta_json, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)

    # Submenús asociados a cada opción del menú principal
    def actualizar_submenu(self, e):
        # Obtiene las opciones del submenú basadas en la selección del primer dropdown
        seleccion = e.control.value

        # Submenús asociados a cada opción del menú principal
        menu = self.cargar_menu_json(self.ruta_json)

        # Actualizar el valor del objeto Text con la opcion elegida
        if seleccion in menu:
            print(menu[seleccion])
            self.subcategoria.options = [ft.dropdown.Option(sub) for sub in menu[seleccion]]
            print(self.subcategoria.options)
        self.subcategoria.update()

    # metodo para registrar nuevo recambio
    def crear_recambio(self, e):
        print("\n > Crear recambio")
        nombre_recambio = self.input_nombreRecambio.content.value.strip()  # este es el Input
        descripcion = self.input_descripcionRecambio.content.value.strip()  # este es el Input
        categoria = self.categoria.content.controls[0].value
        subcategoria = self.subcategoria.value.strip()
        fecha_alta = datetime.now()

        # Creación y adición del nuevo recambio
        nuevo_recambio = Recambio(nombre_recambio=nombre_recambio, descripcion=descripcion, categoria=categoria,
                                  subcategoria=subcategoria, fecha_alta=fecha_alta)
        try:
            db.session.add(nuevo_recambio)
            db.session.commit()
            print("Recambio creado con éxito.")
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error al crear el recambio: {e}")
        finally:
            db.session.close()


class VentanaRecambios(ft.View):
    '''Clase VentanaRecambios: Interfaz gráfica para la gestión de recambios.

    Esta clase representa la ventana de la aplicación dedicada a la gestión de recambios, donde el
    usuario puede realizar operaciones como búsqueda, adición, modificación y eliminación de recambios
    utilizados en las reparaciones.

    Args:
        - page: Instancia de la página actual, que maneja el contenido y las interacciones de la ventana.

    Contiene:
        - Imagen de título: Muestra una imagen de "Recambios" para identificar visualmente la sección.
        - Input: Campo de texto para ingresar el nombre o los detalles del recambio a buscar.
        - Botón ElevatedButton "Buscar Recambio": Activa la búsqueda de recambios en base a los datos ingresados.
        - Botón ElevatedButton "Añadir Recambio": Permite al usuario añadir un nuevo recambio al sistema ingresando
          los datos requeridos (nombre, descripción, costo, etc.).
        - Botón ElevatedButton "Modificar Recambio": Accede a una interfaz para modificar los datos de un
          recambio existente en el sistema.
        - Botón ElevatedButton "Eliminar Recambio": Elimina del sistema los registros del recambio seleccionado.
    '''


    def __init__(self, page: ft.Page):
        '''Constructor de la interfaz grafica para la ventana recambios'''
        super(VentanaRecambios, self).__init__(
            route="/recambios", horizontal_alignment=CrossAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER
        )

        # Ruta completa al archivo JSON del menu para los recambios
        self.ruta_json = r'C:\Users\Juan Carlos\espacio_de_trabajo\AAA Practicas personal\TallerManager\database\menu_recambios.json'

        self.page = page

        # Color de fondo contenedor principal
        self.bgcolor = "#ede0cc"

        # Titulo imagen recambios
        self.imagenRecambios = ft.Container(
            ft.Container(
                bgcolor="#ede0cc",
                width=320,
                height=70,
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
        self.input_buscar = ft.TextField(
            label="Buscar Recambio...",
            label_style=TextStyle(color='#6a6965', size=12),
            value="",
            border_radius=ft.border_radius.vertical(top=5, bottom=5),
            hint_text="Introduce el recambio",
            hint_style=TextStyle(color='#6a6965', size=10),
            color='black',
            height=35,
            cursor_color="#12597b",
            text_size=13,
            border_color="#12597b",
            autofocus=True,
            bgcolor="#E1F5FE"
        )

        # Menu desplegable principal para elegir una opcion
        self.menu_principal = ft.Container(
            alignment=ft.alignment.Alignment(x=0, y=0),
            content=Row(
                alignment=ft.MainAxisAlignment.START,
                controls=[
                    ft.Dropdown(
                        label='Selecciona Categoría',
                        alignment = Alignment(0.0, 0.0),
                        label_style=TextStyle(color='#12597b', size=13, bgcolor= '#ede0cc', weight=ft.FontWeight.W_700),
                        options_fill_horizontally =True,
                        dense = True,
                        height=40,
                        width=300,
                        content_padding=6,
                        color='#12597b',
                        border_color='#12597b',
                        text_size=11,
                        on_change=lambda e: (self.pestaniaOpcion(e),
                                             self.actualizar_submenu(e)),
                        options=[
                            # Lista de opciones para los recambios
                            ft.dropdown.Option("Accesorios para coche"),
                            ft.dropdown.Option("Aceites y líquidos"),
                            ft.dropdown.Option("Aire acondicionado"),
                            ft.dropdown.Option("Amortiguacion"),
                            ft.dropdown.Option("Árboles de transmisión y diferenciales"),
                            ft.dropdown.Option("Caja de cambios"),
                            ft.dropdown.Option("Calefacción y ventilación"),
                            ft.dropdown.Option("Carrocería"),
                            ft.dropdown.Option("Correas, cadenas, rodillos"),
                            ft.dropdown.Option("Direccion"),
                            ft.dropdown.Option("Embrague"),
                            ft.dropdown.Option("Encendido y precalentamiento"),
                            ft.dropdown.Option("Escape"),
                            ft.dropdown.Option("Filtros"),
                            ft.dropdown.Option("Frenos"),
                            ft.dropdown.Option("Herramientas y equipo"),
                            ft.dropdown.Option("Iluminación"),
                            ft.dropdown.Option("Interior"),
                            ft.dropdown.Option("Juntas y retenes"),
                            ft.dropdown.Option("Kit de reparación"),
                            ft.dropdown.Option("Motor"),
                            ft.dropdown.Option("Neumáticos"),
                            ft.dropdown.Option("Palier y junta homocinetica"),
                            ft.dropdown.Option("Productos para cuidado del coche"),
                            ft.dropdown.Option("Remolque / piezas adicionales"),
                            ft.dropdown.Option("Rodamientos"),
                            ft.dropdown.Option("Sensores, relés, unidades de control"),
                            ft.dropdown.Option("Sistema de combustible"),
                            ft.dropdown.Option("Sistema de refrigeración del motor"),
                            ft.dropdown.Option("Sistema electrico"),
                            ft.dropdown.Option("Sistema limpiaparabrisas"),
                            ft.dropdown.Option("Sujeciones"),
                            ft.dropdown.Option("Suspension"),
                            ft.dropdown.Option("Tuberías y mangueras"),
                            ft.dropdown.Option("Tuning")

                        ],
                        bgcolor="#ede0cc",
                        padding = 0,
                    )
                ]
            )
        )

        # Menu desplegable secundario para elegir una opcion
        self.submenu_opciones = ft.Dropdown(
                        label='Selecciona Subcategoría',
                        alignment = Alignment(0.0, 0.0),
                        label_style=TextStyle(color='#12597b', size=12, bgcolor= '#ede0cc', weight=ft.FontWeight.W_700),
                        options_fill_horizontally =True,
                        dense = True,
                        max_menu_height=True,
                        height=50,
                        width=300,
                        content_padding=6,
                        color='#12597b',
                        border_color='#12597b',
                        text_size=10,
                        #on_change=lambda e: (self.actualizar_submenu(e)),
                        options=[],
                        bgcolor="#ede0cc",
                        padding=0,
                    )

        # Boton para activar la busqueda del recambio y boton agregar nuevo recambio
        self.BotonBuscarRecambio = ft.Container(
            alignment=ft.alignment.Alignment(x=0, y=0),
            content=Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    # Boton buscar cliente y añadir nuevo
                    ft.ElevatedButton(
                        text="Buscar Recambio",
                        color="#FAFAF3",
                        bgcolor="#12597b",
                        tooltip='Buscar Recambio',
                        icon=icons.SEARCH,
                        icon_color="#FAFAF3",
                        width=185,
                        height=30,
                        on_click=lambda e: self.buscar_recambio(e),
                    ),
                    # Boton para añadir nuevo recambio a la db
                    ft.IconButton(
                        content=ft.Image(src="add-spare part.png",
                                         color="#12597b",
                                         height=30,
                                         width=30),
                        tooltip="Añadir Nuevo",
                        on_click=lambda _: page.go("/crearRecambio"),
                    ),

                ]
            )
        )

        # Contenedor para mostrar los resultados de búsqueda
        self.vistaResultadosBusqueda = ft.Container(
            bgcolor='#ede0cc',
            expand=True,
            content=ft.GridView(
                expand=1,
                child_aspect_ratio=1.7, # ajusta la relacion alto por ancho
                runs_count=1,  # ajusta el número de columnas según el diseño
                spacing=1,  # Espacio entre las imágenes
                run_spacing=1,  # Espacio entre las filas
            )
        )


        # Barra de navegacion
        self.barraNavegacion = ft.NavigationBar(
            selected_index=3,
            height=50,
            on_change=lambda e: self.barra_de_navegacion(e),
            destinations=[
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.HOME_OUTLINED,
                        color="#12597b",
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
                        color="#12597b",
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
                        color="#12597b",
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
                        color="#12597b",
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
                        color="#12597b",
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
            bgcolor="#ede0cc",  # Color de fondo de la barra de navegación (azul oscuro)
            indicator_color=ft.colors.AMBER_500,  # Color del indicador del destino seleccionado (ámbar)
            surface_tint_color="#ede0cc",  # Color de superficie para el material (#ede0cc)
            label_behavior=ft.NavigationBarLabelBehavior.ONLY_SHOW_SELECTED  # Mostrar la etiqueta  seleccionada
        )

        # Contenedor principal que contiene todos los elementos de la interfaz
        self.controls = [
            ft.Container(
                ft.Column([
                    self.imagenRecambios,
                    self.input_buscar,
                    self.menu_principal,
                    self.submenu_opciones,
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
                    "#ede0cc",
                    "#ede0cc",
                ])

            )
        ]


    # metodo para manejar la opcion seleccionada en el menu desplegable principal
    def pestaniaOpcion(self, e):
        try:
            # Crear un objeto Text para mostrar la opcion elegida
            t = ft.Text()

            # Obtener la opcion elegida del menu desplegable
            elegirOpcion = self.menu_principal.content.controls[0].value

            # Actualizar el valor del objeto Text con la opcion elegida
            t.value = f"Opción elegida: {elegirOpcion}"

            # Diccionario que mapea las opciones a las acciones correspondientes
            acciones = {
                'Neumaticos':'Buscar en Neumaticos',
                'Aceites y liquidos': 'Buscar en Aceites y liquidos',
                'Frenos': 'Buscar en Frenos',
                'Filtros': 'Buscar en Filtros',
                'Motor': 'Buscar en Motor',
                'Sistema limpiaparabrisas': 'Buscar en Sistema limpiparabrisas',
                'Encendido y precalentamiento': 'Buscar en Encendido y precalentamiento',
                'Suspension': 'Buscar en Suspension',
                'Sistema electrico': 'Buscar en Sistema electrico',
                'Amortiguacion': 'Buscar en Amortiguacion',
                'Correas,cadenas,rodillos': 'Buscar en Correas,cadenas,rodillos',
                'Sistema de refrigeracion del motor': 'Buscar en Sistema de refrigeracion del motor',
                'Carroceria': 'Buscar en Carroceria',
                'Calefaccion y ventilacion': 'Buscar en Calefaccion y ventilacion',
                'Juntas y retenes': 'Buscar en Juntas y retenes',
                'Escape': 'Buscar en Escape',
                'Interior': 'Buscar en Interior',
                'Sistema de combustible': 'Buscar en Sistema de combustible',
                'Direccion': 'Buscar en Direccion',
                'Embrague': 'Buscar en Embrague',
                'Palier y junta homocinetica': 'Buscar en Palier y junta homocinetica',
                'Remolque / piezas adicionales': 'buscar en Remolque / piezas adicionales',
                'Caja de cambios': 'Buscar en Caja de cambios',
                'Aire acondicionado': 'Buscar en Aire acondicionado',
                'Rodamientos': 'Buscar en Rodamintos',
                'Arboles de transmision y diferenciales': 'Buscar en Arboles de transmision y diferenciales',
                'Sensores, reles, unidades de control': 'Buscar en Sensores, reles, unidades de control',
                'Accesorios para coche': 'Buscar en Accesorios para coche',
                'Kit de reparacion': 'Buscar en Kit de reparacion',
                'Herramientas y equipo': 'Buscar en Herramientas y equipo',
                'Tuberias y mangueras': 'Buscar en Tuberis y mangueras',
                'Productos para cuidado del coche': 'Buscar en Productos para cuidado del coche',
                'Iluminación': 'Buscar en Iluminación',
                'Tuning': 'Buscar en Tuning',
                'Sujeciones': 'Buscar en Sujeciones',
            }

            # Imprimir un mensaje segun la opcion elegida
            if elegirOpcion in acciones:
                print(acciones[elegirOpcion])
            else:
                print('Opcion no valida')

            # Actualizar la pagina con el objeto Text
            self.page.update(self)
            # Agregar el objeto Text a la pagina
            self.page.add(t)
        except Exception as e:
            print(f'Error: {e}')
            # Registrar el error en el archivo de texto
            with open("errores.txt", "a") as file:
                momentoEspecificoError = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                nombre_metodo = "pestaniaOpcion, VentanaRecambios"
                mensaje_error = f"{momentoEspecificoError} - Método: {nombre_metodo} - Error general: {e}\n"
                file.write(mensaje_error)
        finally:
            db.session.close()

    # metodo para cargar el menu de recambios en .json
    def cargar_menu_json(self, ruta_json):
        with open(ruta_json, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)

    # Submenús asociados a cada opción del menú principal
    def actualizar_submenu(self, e):
        # Obtiene las opciones del submenú basadas en la selección del primer dropdown
        seleccion = e.control.value

        # Submenús asociados a cada opción del menú principal
        menu = self.cargar_menu_json(self.ruta_json)

        # Actualizar el valor del objeto Text con la opcion elegida
        if seleccion in menu:
            print(menu[seleccion])
            self.submenu_opciones.options = [ft.dropdown.Option(sub) for sub in menu[seleccion]]
            print(self.submenu_opciones.options)

        else:
            self.submenu_opciones.options = []  # Si no hay submenú, vacía las opciones
        self.submenu_opciones.value = None  # Resetea la selección del submenú
        self.submenu_opciones.update()

    # metodo para el evento de clic del boton de busqueda
    def botonBuscar(self, e):
        categoria = self.menu_principal.content.controls[0].value

        categorias = ['Accesorios para coche', 'Aceites y liquidos', 'Aire acondicionado', 'Amortiguacion',
                      'Arboles de transmision y diferenciales', 'Caja de cambios', 'Calefaccion y ventilacion',
                      'Carroceria', 'Correas, cadenas, rodillos', 'Direccion', 'Embrague', 'Encendido y precalentamiento',
                      'Escape', 'Filtros', 'Frenos', 'Herramientas y equipo', 'Iluminacion', 'Interior', 'Juntas y retenes',
                      'Kit de reparacion', 'Motor', 'Neumaticos', 'Palier y junta homocinetica', 'Productos para cuidado del coche',
                      'Remolque / piezas adicionales', 'Rodamientos', 'Sensores, reles, unidades de control', 'Sistema de conbustible',
                      'Sistema de refrigeracion de motor', 'Sistema electrico', 'Sistema limpiaparabrisas', 'Sujeciones', 'Suspension',
                      'Tuberias y mangueras', 'Tuning']

        # Realizar la búsqueda segun la categoria seleccionada
        if categoria in categorias:
                self.buscar_recambio(e)
        else:
            print('Opción no válida, elige categoria en el desplegable')

    # metodo para cargar los recambios existentes en el GridView
    def buscar_recambio(self,e):
        # Limpia los controles actuales del GridView
        self.vistaResultadosBusqueda.content.controls = []

        # inputs donde el usuario ingresa el nombre, categoria y subcategoria del recambio que quiere buscar
        recambio = self.input_buscar.value.strip()  # este es el Input
        categoria = self.menu_principal.content.controls[0].value.strip()
        subcategoria = (self.submenu_opciones.value.strip() if self.submenu_opciones.value else "")

        # Buscamos el recambio por nombre (ignorando mayúsculas y minusculas)
        recambio_localizado = db.session.query(Recambio).filter(
            and_(
                Recambio.nombre_recambio.ilike(f'%{recambio}%'),
                Recambio.categoria.ilike(f'%{categoria}%'),
                or_(
                    Recambio.subcategoria.ilike(f'%{subcategoria}%'),
                    Recambio.subcategoria.is_(None)  # Opcional: permite que sea None si no se proporciona un valor
                )
            )
        ).all()


        self.input_buscar.value = ""
        self.input_buscar.update()

        if recambio_localizado:
            cards = []
            for recambios in recambio_localizado:
                # mostramos detalles del cliente encontrado
                print(f"Nombre: {recambios.nombre_recambio}, Desde: {recambios.fecha_alta.strftime('%d/%m/%Y')}")
                card = ft.Card(
                    content=ft.Container(
                        alignment=ft.alignment.Alignment(x=0, y=0),
                        bgcolor="#4b8ca8",
                        padding=5,
                        border=ft.border.all(1, ft.colors.BLUE_800),
                        border_radius=ft.border_radius.all(10),
                        content=ft.Column([
                            ft.Container(
                                ft.Row(
                                    [
                                        ft.Text(f"Desde: {recambios.fecha_alta.strftime('%d/%m/%Y')}",size=11, weight=ft.FontWeight.W_700, text_align=ft.TextAlign.START),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                bgcolor="transparent",
                                alignment=ft.alignment.center
                            ),
                            ft.Container(
                                ft.Row(
                                    [
                                        ft.Text(f"ID:", size=10, weight=ft.FontWeight.W_700,text_align=ft.TextAlign.LEFT),
                                        ft.Text(f"{recambios.id_recambio}",size=10, text_align=ft.TextAlign.LEFT),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                bgcolor="transparent",
                                padding=0,
                                alignment=ft.alignment.center_left,

                            ),
                            ft.Container(
                                ft.Row(
                                    [
                                        ft.Text(f"Nombre:", size=10, weight=ft.FontWeight.W_700, text_align=ft.TextAlign.LEFT),
                                        ft.Text(f"{recambios.nombre_recambio}",size=10, text_align=ft.TextAlign.CENTER, no_wrap = False) # no_wrap Asegura que el texto se ajuste si es largo
                                    ],
                                    wrap=True,  # asegura que el contenido se ajuste en varias filas si es necesario
                                    alignment=ft.MainAxisAlignment.START,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                bgcolor="transparent",
                                padding=0,
                                alignment=ft.alignment.center_left,
                            ),
                            ft.Container(
                                ft.Row(
                                    [
                                        ft.Text(f"Descripcion:", size=10, weight=ft.FontWeight.W_700,
                                                text_align=ft.TextAlign.LEFT),
                                        ft.Text(f"{recambios.descripcion}", size=10, text_align=ft.TextAlign.LEFT,  no_wrap = False) # no_wrap Asegura que el texto se ajuste si es largo)
                                    ],
                                    wrap=True, # asegura que el contenido se ajuste en varias filas si es necesario
                                    alignment=ft.MainAxisAlignment.START,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                expand=True,
                                bgcolor="transparent",
                                padding=1,
                                alignment=ft.alignment.center_left,
                            ),

                            ft.Row([
                                ft.ElevatedButton(
                                    bgcolor="#12597b",
                                    width=95,
                                    height=20,
                                    content=ft.Text("Asignar", color="white", size=11, bgcolor="#12597b")),# on_click=lambda: editar_cliente(cliente)),
                                ft.ElevatedButton(
                                    bgcolor="#12597b",
                                    width=80,
                                    height=20,
                                    content=ft.Text("Editar", color="white", size=11, bgcolor="#12597b"))
                            ],
                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                vertical_alignment=ft.CrossAxisAlignment.END,
                            )
                        ])
                    )
                )

                cards.append(card)

            # agregar cards al GridView
            for card in cards:
                self.vistaResultadosBusqueda.content.controls.append(card)
            #actualizar la interfaz
            self.vistaResultadosBusqueda.update()

    # metodo para navegar entre ventanas
    def barra_de_navegacion(self, e):
        selected_index = e.control.selected_index
        if selected_index == 0:
            self.page.go("/inicio")
        elif selected_index == 1:
            self.page.go("/clientes")
        elif selected_index == 2:
            self.page.go("/vehiculos")
        elif selected_index == 3:
            self.page.go("/recambios")
        elif selected_index == 4:
            self.page.go("/ingresos")


class VentanaIngreso(ft.View):
    '''Clase VentanaIngreso: Interfaz gráfica para la gestión de ingresos de vehículos al taller.

    Esta clase representa la ventana de la aplicación dedicada a la gestión de ingresos, permitiendo
    al usuario registrar, buscar, modificar y eliminar los ingresos de vehículos en el taller.

    Args:
        - page: Instancia de la página actual, que gestiona el contenido y las interacciones de la ventana.

    Contiene:
        - Imagen de diagnóstico de ingresos como título: Identifica la sección de ingresos con una imagen adecuada.
        - Input: Campo de texto para buscar ingresos por criterios como fecha, matrícula del vehículo o diagnóstico.
        - Botón ElevatedButton "Buscar Ingreso": Activa la búsqueda de ingresos basados en los datos ingresados.
        - Botón ElevatedButton "Añadir Ingreso": Permite añadir un nuevo registro de ingreso de un vehículo al taller,
          incluyendo detalles como fecha, avería reportada y diagnóstico.
        - Botón ElevatedButton "Modificar Ingreso": Accede a una interfaz para modificar los detalles de un ingreso
          ya registrado.
        - Botón ElevatedButton "Eliminar Ingreso": Elimina del sistema el ingreso seleccionado.
    '''


    def __init__(self, page: ft.Page):
        '''Constructor de la interfaz grafica para la ventana Ingresos'''
        super(VentanaIngreso, self).__init__(
            route="/ingresos", horizontal_alignment=CrossAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER
        )

        self.page = page

        # Color de fondo contenedor principal
        self.bgcolor = "#ede0cc"

        # Titulo imagen ingresos
        self.imagenVehiculos = ft.Container(
            ft.Container(
                bgcolor="#ede0cc",
                width=320,
                height=70,
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
            height=35,
            cursor_color="#12597b",
            text_size=13,
            border_color="#12597b",
            autofocus=True,
            bgcolor="#E1F5FE"
        )

        # Boton para activar la busqueda del ingreso y agregar nuevo ingreso
        self.BotonBuscarVehiculo = ft.Container(
            alignment=ft.alignment.Alignment(x=0, y=0),
            content=Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    # Boton buscar cliente y añadir nuevo
                    ft.ElevatedButton(
                        text="Buscar Ingreso",
                        color="#FAFAF3",
                        bgcolor="#12597b",
                        tooltip='Buscar Ingreso',
                        icon=icons.SEARCH,
                        icon_color="#FAFAF3",
                        width=180,
                        height=30,
                        on_click=lambda e: self.buscar_ingreso_porMatricula(e),
                    ),
                    ft.IconButton(
                        content=ft.Image(src="add-new entry.png",
                                         color= "#12597b",
                                         height=30,
                                         width=30),
                        tooltip="Añadir Nuevo",
                        on_click=lambda _: page.go("/nuevo_ingreso"),
                        )
                ]
            )
        )

        # Contenedor para mostrar los resultados de busqueda
        self.vistaResultadosBusqueda = ft.Container(
            bgcolor='#ede0cc',
            expand=True,
            content=ft.GridView(
                expand=1,
                child_aspect_ratio=1.7, # ajusta la relacion alto por ancho
                runs_count=1,  # ajusta el número de columnas según el diseño
                spacing=1,  # Espacio entre las imágenes
                run_spacing=1,  # Espacio entre las filas
            )
        )

        # Barra de navegacion
        self.barraNavegacion = ft.NavigationBar(
            selected_index=4,
            height=50,
            on_change=lambda e: self.barra_de_navegacion(e),
            destinations=[
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.HOME_OUTLINED,
                        color="#12597b",
                        size=20
                    ),
                    selected_icon_content=ft.Icon(
                        name=ft.icons.HOME_ROUNDED,
                        color="#12597b",
                        size=24
                    ),
                    label="Inicio",
                ),
                ft.NavigationBarDestination(
                    icon_content=ft.Icon(
                        name=ft.icons.PERSON_OUTLINED,
                        color="#12597b",
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
                        color="#12597b",
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
                        color="#12597b",
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
                        color="#12597b",
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
            bgcolor="#ede0cc",  # Color de fondo de la barra de navegación (azul oscuro)
            indicator_color=ft.colors.AMBER_500,  # Color del indicador del destino seleccionado (ámbar)
            surface_tint_color="#ede0cc",  # Color de superficie para el material (#ede0cc)
            label_behavior=ft.NavigationBarLabelBehavior.ONLY_SHOW_SELECTED  # Mostrar la etiqueta  seleccionada
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

                # propiedades del contenedor principal
                border_radius=25,
                width=350,  # ancho
                height=655,  # Alto
                gradient=ft.LinearGradient([  # color del contenedor configurable en 2 tonos de color
                    "#ede0cc",
                    "#ede0cc",
                ])

            )
        ]

    # metodo para cargar los ingresos existentes por cliente en el GridView
    def buscar_ingreso_porCliente(self):
        print("\n > Buscar ingreso por cliente")

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

    # metodo para cargar los ingresos existentes por matricula en el GridView
    def buscar_ingreso_porMatricula(self, e):
        print("\n > Buscar ingreso por matricula")

        # Limpia los controles actuales del GridView
        self.vistaResultadosBusqueda.content.controls = []

        # input del vehiculo que quiere buscar
        matricula_vehiculo = self.input_buscar.value.strip()  # este es el Input

        if not matricula_vehiculo:
            print("Ingrese una matrícula válida")
        else:
            # Buscamos el vehiculo por matricula (ignorando mayúsculas y minusculas)
            vehiculo_ingresado = db.session.query(Ingreso).join(Vehiculo).join(Cliente).filter(
            Vehiculo.matricula.ilike(f'%{matricula_vehiculo}%')
            ).all()

            self.input_buscar.value = ""
            self.input_buscar.update()

            if vehiculo_ingresado:
                print("\nResultados de la búsqueda:")


                # Crear una lista de Cards para los resultados de busqueda
                cards = []
                for ingreso in vehiculo_ingresado:
                    # accede a las relaciones asociadas del objeto
                    cliente = ingreso.clientes
                    vehiculo = ingreso.vehiculos
                    print(
                        f"Ingreso ID: {ingreso.id_ingreso}, "
                        f"\nFecha Ingreso: {ingreso.fecha_ingreso.strftime('%d/%m/%Y')}"
                        f"\ncliente: {cliente.nombre}"
                        f"\nVehiculo: {vehiculo.marca}, {vehiculo.modelo}"
                        f"\nMatricula: {vehiculo.matricula}"
                        f"\nDiagnostico: {ingreso.diagnostico}"
                        f"\nKilometros Ingreso: {ingreso.kilometros_ingreso}")

                    card = ft.Card(
                        content=ft.Container(
                            alignment=ft.alignment.Alignment(x=0, y=0),
                            bgcolor="#4b8ca8",
                            padding=5,
                            border=ft.border.all(1, ft.colors.BLUE_800),
                            border_radius=ft.border_radius.all(10),
                            content=ft.Column([
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.Text(f"Cliente: {cliente.nombre}",
                                                    size=11,
                                                    weight=ft.FontWeight.W_700, text_align=ft.TextAlign.START
                                                    ),
                                            ft.Text(f"Fecha Ingreso: {ingreso.fecha_ingreso.strftime('%d/%m/%Y')}", size=11,
                                                    weight=ft.FontWeight.W_700, text_align=ft.TextAlign.START
                                                    ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                    bgcolor="transparent",
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.Text(f"Marca y modelo:", size=10, weight=ft.FontWeight.W_700,
                                                    text_align=ft.TextAlign.LEFT),
                                            ft.Text(f"{vehiculo.marca}, {vehiculo.modelo}", size=10,
                                                    text_align=ft.TextAlign.LEFT)
                                        ],
                                        alignment=ft.MainAxisAlignment.START,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                    bgcolor="transparent",
                                    padding=0,
                                    alignment=ft.alignment.center_left,
                                ),
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.Text(f"Matricula:", size=10, weight=ft.FontWeight.W_700,
                                                    text_align=ft.TextAlign.LEFT),
                                            ft.Text(f"{vehiculo.matricula}", size=10,
                                                    text_align=ft.TextAlign.LEFT)
                                        ],
                                        alignment=ft.MainAxisAlignment.START,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                    bgcolor="transparent",
                                    padding=0,
                                    alignment=ft.alignment.center_left,
                                ),
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.Text(f"Diagnostico:", size=10, weight=ft.FontWeight.W_700,
                                                    text_align=ft.TextAlign.LEFT),
                                            ft.Text(f"{ingreso.diagnostico}", size=10, text_align=ft.TextAlign.LEFT),
                                        ],
                                        alignment=ft.MainAxisAlignment.START,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                    bgcolor="transparent",
                                    padding=0,
                                    alignment=ft.alignment.center_left,

                                ),
                                ft.Container(
                                    ft.Row(
                                        [
                                            ft.Text(f"Kilometros:", size=10, weight=ft.FontWeight.W_700,
                                                    text_align=ft.TextAlign.LEFT),
                                            ft.Text(f"{ingreso.kilometros_ingreso}", size=10, text_align=ft.TextAlign.LEFT)
                                        ],
                                        alignment=ft.MainAxisAlignment.START,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                    bgcolor="transparent",
                                    padding=0,
                                    alignment=ft.alignment.center_left,
                                ),
                                ft.Row(
                                    [
                                        ft.ElevatedButton(
                                            bgcolor="#12597b",
                                            width=95,
                                            height=20,
                                            content=ft.Text("Ver", color="white", size=11, bgcolor="#12597b")),
                                        # on_click=lambda: editar_cliente(cliente)),
                                        ft.ElevatedButton(
                                            bgcolor="#12597b",
                                            width=80,
                                            height=20,
                                            content=ft.Text("Editar", color="white", size=11, bgcolor="#12597b"))
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                    vertical_alignment=ft.CrossAxisAlignment.END,
                                )
                            ])
                        )
                    )

                    cards.append(card)

                # agregar cards al GridView
                for card in cards:
                    self.vistaResultadosBusqueda.content.controls.append(card)
                # actualizar la interfaz
                self.vistaResultadosBusqueda.update()

    # metodo para navegar entre ventanas
    def barra_de_navegacion(self, e):
        selected_index = e.control.selected_index
        if selected_index == 0:
            self.page.go("/inicio")
        elif selected_index == 1:
            self.page.go("/clientes")
        elif selected_index == 2:
            self.page.go("/vehiculos")
        elif selected_index == 3:
            self.page.go("/recambios")
        elif selected_index == 4:
            self.page.go("/ingresos")


class VentanaNuevoIngreso(ft.View):
    '''Clase VentanaNuevoIngreso: Interfaz gráfica para la gestión de ingresos nuevos de vehículos al taller.

    Esta clase representa la ventana de la aplicación dedicada a la gestión de nuevos ingresos, permitiendo
    al usuario registrar los vehículos en el taller y asociarlos con clientes específicos.

    Args:
        - page: Instancia de la página actual, que gestiona el contenido y las interacciones de la ventana.

    Contiene:
        - Imagen de diagnóstico de ingresos como título: Identifica la sección de ingreso nuevo con una imagen representativa.
        - Dropdown Cliente: Desplegable para seleccionar el cliente que ingresa el vehículo al taller.
        - Dropdown Vehículo: Desplegable para seleccionar el vehículo del cliente que será ingresado al taller.
        - Input Kilometraje: Campo de texto para introducir el kilometraje actual del vehículo al momento del ingreso.
        - Input Motivo de Ingreso: Campo de texto para introducir el motivo por el cual el vehículo acude al taller.
        - Input Diagnóstico Previo: Campo de texto para introducir el diagnóstico inicial del taller antes del ingreso.
        - Botón Aceptar: Botón para confirmar y registrar el ingreso.
    '''


    def __init__(self, page: ft.Page):
        '''Constructor de la interfaz grafica para la ventana Ingresos'''
        super(VentanaNuevoIngreso, self).__init__(
            route="/nuevo_ingreso", horizontal_alignment=CrossAxisAlignment.CENTER,
            vertical_alignment=MainAxisAlignment.CENTER
        )

        self.page = page

        # Color de fondo contenedor principal
        self.bgcolor = "#ede0cc"

        # Titulo imagen ingresos
        self.imagenVehiculos = ft.Container(
            ft.Container(
                bgcolor="#ede0cc",
                width=320,
                height=70,
                padding=0,
                image_repeat=ImageRepeat.NO_REPEAT,
                shape=ft.BoxShape("rectangle"),
                # Define imagen
                image_src="/Imagen_de_nuevo_ingreso.png",
                image_fit=ft.ImageFit.COVER,
            ),
            alignment=ft.alignment.Alignment(x=0, y=0)
        )

        # Objeto Text para mostrar la opción elegida
        self.texto_opcion_elegida = ft.Text()

        # menu desplegable principal para elegir un cliente
        self.menu_clientes= ft.Container(
            alignment=ft.alignment.Alignment(x=0, y=0),
            content=Row(
                alignment=ft.MainAxisAlignment.START,
                controls=[
                    ft.Dropdown(
                        label='Selecciona un Cliente',
                        alignment=Alignment(0.0, 0.0),
                        label_style=TextStyle(color='#12597b', size=12, bgcolor='#ede0cc', weight=ft.FontWeight.W_700),
                        options_fill_horizontally=True,
                        dense=True,
                        max_menu_height=True,
                        height=50,
                        width=300,
                        content_padding=6,
                        color='#12597b',
                        border_color='#12597b',
                        text_size=10,
                        on_change=lambda e: (self.pestaniaOpcion(e), self.cargar_menu_vehiculos(e)),
                        options=[ft.dropdown.Option(str(cliente.nombre))
                            for cliente in db.session.query(Cliente).all()],
                        bgcolor="#ede0cc",
                        padding=0,
                    )
                ]
            )
        )


        # menu desplegable para seleccionar el vehiculo
        self.menu_vehiculosCliente= ft.Dropdown(
                        label='Selecciona un Vehiculo',
                        alignment = Alignment(0.0, 0.0),
                        label_style=TextStyle(color='#12597b', size=12, bgcolor= '#ede0cc', weight=ft.FontWeight.W_700),
                        options_fill_horizontally =True,
                        dense = True,
                        max_menu_height=True,
                        height=50,
                        width=300,
                        content_padding=6,
                        color='#12597b',
                        border_color='#12597b',
                        text_size=10,
                        #on_change=lambda e: (self.actualizar_submenu(e)),
                        options=[],
                        bgcolor="#ede0cc",
                        padding=0,
                    )

        # Campo de entrada para la busqueda
        self.input_kilometros = ft.TextField(
            label="Kilometros...",
            label_style=TextStyle(color='#6a6965', size=12),
            value="",
            border_radius=ft.border_radius.vertical(top=0, bottom=0),
            hint_text="Introduce los kilometros del vehiculo",
            hint_style=TextStyle(color='#6a6965', size=10),
            color='black',
            height=35,
            cursor_color="#12597b",
            text_size=13,
            border_color="#12597b",
            autofocus=True,
            bgcolor="#E1F5FE"
        )

        # Campo de entrada del motivo de la averia reportada por el cliente
        self.input_motivo = ft.Container(
            bgcolor='#FAFAF3',
            # border=ft.border.all(ft.colors.ORANGE_100),
            #expand=True,
            height=180,
            content=
                ft.TextField(
                    filled=False,
                    label="Motivo...",
                    label_style=TextStyle(color='#12597b', size=12, ),
                    expand=True,
                    value="",
                    border_radius=ft.border_radius.vertical(top=5, bottom=5),
                    hint_text="Introduce el motivo de la averia reportada por el cliente",
                    hint_style=TextStyle(color='#6a6965', size=10),
                    max_length=180,  # maximo de caracteres que se pueden ingresar en TextField
                    # max_lines =  10, # maximo de líneas que se mostraran a la vez
                    multiline=True,  # puede contener varias lineas de texto
                    color='black',
                    height=180,
                    cursor_color="#12597b",
                    text_size=13,
                    border_color="transparent",
                    autofocus=False,
                    bgcolor="transparent",
                    text_vertical_align=ft.VerticalAlignment.START,
                )
            )

        # Campo de entrada del diagnostico del vehiculo por taller
        self.input_diagnotico = ft.Container(
            bgcolor='#FAFAF3',
            # border=ft.border.all(ft.colors.ORANGE_100),
            # expand=True,
            height=180,
            content=
            ft.TextField(
                filled=False,
                label="Diagnostico...",
                label_style=TextStyle(color='#12597b', size=12, ),
                expand=True,
                value="",
                border_radius=ft.border_radius.vertical(top=5, bottom=5),
                hint_text="Introduce el diagnostico del vehiculo por taller",
                hint_style=TextStyle(color='#6a6965', size=10),
                max_length=180,  # maximo de caracteres que se pueden ingresar en TextField
                # max_lines =  10, # maximo de líneas que se mostraran a la vez
                multiline=True,  # puede contener varias lineas de texto
                color='black',
                height=180,
                cursor_color="#12597b",
                text_size=13,
                border_color="transparent",
                autofocus=False,
                bgcolor="transparent",
                text_vertical_align=ft.VerticalAlignment.START,
            )
        )

        # Boton para activar la busqueda del ingreso y agregar nuevo nuevo ingreso
        self.BotonAgregarVehiculo = ft.Container(
            alignment=ft.alignment.Alignment(x=0, y=0),
            content=Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    # Boton buscar cliente y añadir nuevo
                    ft.ElevatedButton(
                        text="Aceptar",
                        color="#FAFAF3",
                        bgcolor="#12597b",
                        tooltip='Aceptar Ingreso',
                        icon=icons.ADD,
                        icon_color="#FAFAF3",
                        width=140,
                        height=30,
                        on_click=lambda e: (self.ingreso_nuevo(e), page.go("/ingresos")),
                    ),
                    ft.ElevatedButton(
                        text="Cancelar",
                        color="#FAFAF3",
                        bgcolor="#12597b",
                        tooltip='Cancelar Ingreso',
                        icon=icons.CANCEL,
                        icon_color="#FAFAF3",
                        width=140,
                        height=30,
                        on_click=lambda _: page.go("/ingresos"),
                    ),
                ]
            )
        )

        # Contenedor para mostrar los resultados de busqueda
        self.vistaResultadosBusqueda = ft.Container(
            bgcolor='#ede0cc',
            expand=True,
            content=ft.GridView(
                expand=1,
                child_aspect_ratio=1.7, # ajusta la relacion alto por ancho
                runs_count=1,  # ajusta el número de columnas según el diseño
                spacing=1,  # Espacio entre las imágenes
                run_spacing=1,  # Espacio entre las filas
            )
        )



        # Contenedor principal que contiene todos los elementos de la interfaz
        self.controls = [
            ft.Container(
                ft.Column([
                    self.imagenVehiculos,
                    self.menu_clientes,
                    self.menu_vehiculosCliente,
                    self.input_kilometros,
                    self.input_motivo,
                    self.input_diagnotico,
                    self.BotonAgregarVehiculo,
                    self.vistaResultadosBusqueda,
                ]
                ),

                # propiedades contenedor principal
                border_radius=25,
                width=350,  # ancho
                height=655,  # Alto
                gradient=ft.LinearGradient([  # color del contenedor configurable en 2 tonos de color
                    "#ede0cc",
                    "#ede0cc",
                ])

            )
        ]

    # metodo para manejar la opcion seleccionada en el menu desplegable
    def pestaniaOpcion(self, e):
        # Obtener la opción seleccionada
        elegirOpcion = self.menu_clientes.content.controls[0].value

        # Actualizar texto con la opción elegida
        self.texto_opcion_elegida.value = (
            f"Opción elegida: {elegirOpcion}" if elegirOpcion else "No se ha seleccionado ninguna opción."
        )

        # Imprime la opción seleccionada
        print(f"Cliente seleccionado: {elegirOpcion}")

        # Actualiza la interfaz
        self.page.update(self)


    # metodo para cargar los vehículos asociados al cliente seleccionado en el dropdown de vehículos
    def cargar_menu_vehiculos(self, e):
        # Obtiene el nombre del cliente seleccionado
        cliente_nombre = e.control.value
        cliente_seleccionado = db.session.query(Cliente).filter_by(nombre=cliente_nombre).first()

        # Verifica si se encontró un cliente y luego obtiene sus vehículos
        if cliente_seleccionado:
            vehiculos = db.session.query(Vehiculo).filter_by(id_cliente=cliente_seleccionado.id_cliente).all()

            # Asigna las opciones de vehículos al dropdown correspondiente
            self.menu_vehiculosCliente.options = [ft.dropdown.Option(f"{vehiculo.marca}, {vehiculo.modelo}") for vehiculo in vehiculos]
        else:
            # Si no hay un cliente válido, limpia las opciones del dropdown de vehículos
            self.menu_vehiculosCliente.options = []

        # Actualiza el dropdown para reflejar los nuevos cambios
        self.menu_vehiculosCliente.update()

    # metodo para añadir nuevo ingreso
    def ingreso_nuevo(self, e):
        print("\n > Crear ingreso")
        id_cliente = self.menu_clientes.content.controls[0].value.strip()
        id_vehiculo = self.menu_vehiculosCliente.value.strip()
        kilometros_ingreso = self.input_kilometros.value.strip()
        averia = self.input_motivo.content.value.strip()
        diagnostico = self.input_diagnotico.content.value.strip()
        fecha_ingreso = datetime.now()

        # Consulta para obtener el cliente y el vehículo seleccionados
        cliente = db.session.query(Cliente).filter_by(nombre=id_cliente).first()
        # el dropdown incluye la marca y modelo per filtra solo por modelo
        vehiculo_modelo = id_vehiculo.split(", ")[1]  # Extrae solo el modelo
        vehiculo = db.session.query(Vehiculo).filter_by(modelo=vehiculo_modelo).first()

        # Validación
        if not cliente or not vehiculo:
            print("Error: Cliente o Vehículo no encontrado.")
            return
        if not kilometros_ingreso or not averia:
            print("Error: Kilómetros o Motivo de avería no proporcionado.")
            return

        # Creación y adición del nuevo recambio
        nuevo_ingreso = Ingreso(kilometros_ingreso=kilometros_ingreso, averia=averia, diagnostico=diagnostico,fecha_ingreso=fecha_ingreso)
        db.session.add(nuevo_ingreso)

        # Relación bidireccional automática
        cliente.ingresos.append(nuevo_ingreso)
        vehiculo.ingresos.append(nuevo_ingreso)
        # Guardar cambios
        db.session.commit()
        db.session.close()
        print("Ingreso creado exitosamente.")


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
        elif page.route == "/clienteNuevo":
            clienteNuevo = VentanaClienteNuevo(page)
            page.views.append(clienteNuevo)
        elif page.route == "/vehiculos":
            vehiculos = VentanaVehiculo(page)
            page.views.append(vehiculos)
        elif page.route == "/vehiculoNuevo":
            vehiculoNuevo = VentanaVehiculoNuevo(page)
            page.views.append(vehiculoNuevo)
        elif page.route == "/recambios":
            recambios = VentanaRecambios(page)
            page.views.append(recambios)
        elif page.route == "/crearRecambio":
            crearRecambio = VentanaCrearRecambio(page)
            page.views.append(crearRecambio)
        elif page.route == "/ingresos":
            ingresos = VentanaIngreso(page)
            page.views.append(ingresos)
        elif page.route == "/nuevo_ingreso":
            nuevo_ingreso = VentanaNuevoIngreso(page)
            page.views.append(nuevo_ingreso)

        page.update()

    page.on_route_change = router
    page.go("/inicio")
    #page.go("/clientes")
    #page.go("/clienteNuevo")
    #page.go("/vehiculos")
    #page.go("/vehiculoNuevo")
    #page.go("/recambios")
    #page.go("/crearRecambio")
    #page.go("/ingresos")
    #page.go("/nuevo_ingreso")


# instanciar y ejecutar la aplicación
ft.app(target=main, assets_dir="assets")

