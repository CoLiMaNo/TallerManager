import datetime
import flet as ft
from flet import *
from sqlalchemy import and_, desc, asc, or_
from sqlalchemy.exc import SQLAlchemyError
from models import Cliente, Vehiculo, Recambio, Ingreso, Registro
import db
import os


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

    # funcion para navegar entre ventanas
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
        - Input: Campo de texto para ingresar el nombre o los datos del cliente a buscar.
        - Botón ElevatedButton "Buscar Cliente": Activa la búsqueda de clientes según los datos ingresados
          en el campo de búsqueda.
        - Botón ElevatedButton "Añadir Cliente": Permite al usuario añadir un nuevo cliente al sistema
          ingresando los datos requeridos (nombre, teléfono, dirección, etc.).
        - Botón ElevatedButton "Modificar Cliente": Accede a una interfaz para modificar los datos de un
          cliente existente en el sistema.
        - Botón ElevatedButton "Eliminar Cliente": Elimina del sistema los registros del cliente seleccionado.
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
                        #on_click=lambda e: self.crear_cliente(e),
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

    # metodo para añadir nuevo cliente
    def crear_cliente(self):
        pass

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
                                        ft.Text(f"{cliente.nombre}, ", size=12, weight=ft.FontWeight.W_700, text_align=ft.TextAlign.CENTER),
                                        ft.Text(f"Desde: {cliente.fecha_alta.strftime('%d/%m/%Y')}", size=10, text_align=ft.TextAlign.LEFT)
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
                                        ft.Text(f"{cliente.direccion}",size=10, text_align=ft.TextAlign.LEFT)
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
                                        ft.Text(f"Correo:", size=10, weight=ft.FontWeight.W_700,
                                                text_align=ft.TextAlign.LEFT),
                                        ft.Text(f"{cliente.correo}", size=10, text_align=ft.TextAlign.LEFT)
                                    ],
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
                                    ft.ElevatedButton(
                                        bgcolor="#12597b",
                                        width=95,
                                        height=20,
                                        content= ft.Text("Ingresos", color="white", size=11,bgcolor="#12597b")), #on_click=lambda: editar_cliente(cliente)),
                                    ft.ElevatedButton(
                                        bgcolor="#12597b",
                                        width=100,
                                        height=20,
                                        content=ft.Text("Vehiculos", color="white", size=11,bgcolor="#12597b")),
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
                        #on_click=lambda e: self.crear_vehiculo(e),
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

    # funcion para navegar entre ventanas
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

    # metodo para cargar los vehiculos existentes en el GridView
    def buscar_vehiculo(self,e):
        # Limpia los controles actuales del GridView
        self.vistaResultadosBusqueda.content.controls = []

        # input donde el usuario ingresa el nombre del cliente que quiere buscar
        matricula_vehiculo = self.input_buscar.value  # este es el Input

        # Buscamos el cliente por nombre (ignorando mayúsculas y minusculas)
        vehiculo_localizado = db.session.query(Vehiculo).filter(
            Vehiculo.matricula.ilike(f'%{matricula_vehiculo}%')).all()

        self.input_buscar.value = ""
        self.input_buscar.update()

        if vehiculo_localizado:
            cards = []
            for vehiculo in vehiculo_localizado:
                # mostramos detalles del cliente encontrado
                print(f"Nombre: {vehiculo.matricula}, Desde: {vehiculo.fecha_alta.strftime('%d/%m/%Y')}")
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
                                        ft.Text(f"Desde: {vehiculo.fecha_alta.strftime('%d/%m/%Y')}",size=11, weight=ft.FontWeight.W_700, text_align=ft.TextAlign.START)
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
                        label='Elige una Opcion',
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
                            ft.dropdown.Option("Aceites y liquidos"),
                            ft.dropdown.Option("Aire acondicionado"),
                            ft.dropdown.Option("Amortiguacion"),
                            ft.dropdown.Option("Arboles de transmision y diferenciales"),
                            ft.dropdown.Option("Caja de cambios"),
                            ft.dropdown.Option("Calefaccion y ventilacion"),
                            ft.dropdown.Option("Carroceria"),
                            ft.dropdown.Option("Correas, cadenas, rodillos"),
                            ft.dropdown.Option("Direccion"),
                            ft.dropdown.Option("Embrague"),
                            ft.dropdown.Option("Encendido y precalentamiento"),
                            ft.dropdown.Option("Escape"),
                            ft.dropdown.Option("Filtros"),
                            ft.dropdown.Option("Frenos"),
                            ft.dropdown.Option("Herramientas y equipo"),
                            ft.dropdown.Option("Iluminacion"),
                            ft.dropdown.Option("Interior"),
                            ft.dropdown.Option("Juntas y retenes"),
                            ft.dropdown.Option("Kit de reparacion"),
                            ft.dropdown.Option("Motor"),
                            ft.dropdown.Option("Neumaticos"),
                            ft.dropdown.Option("Palier y junta homocinetica"),
                            ft.dropdown.Option("Productos para cuidado del coche"),
                            ft.dropdown.Option("Remolque / piezas adicionales"),
                            ft.dropdown.Option("Rodamientos"),
                            ft.dropdown.Option("Sensores, reles, unidades de control"),
                            ft.dropdown.Option("Sistema de conbustible"),
                            ft.dropdown.Option("Sistema de refrigeracion del motor"),
                            ft.dropdown.Option("Sistema electrico"),
                            ft.dropdown.Option("Sistema limpiaparabrisas"),
                            ft.dropdown.Option("Sujeciones"),
                            ft.dropdown.Option("Suspension"),
                            ft.dropdown.Option("Tuberias y mangueras"),
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
                        label='Submenú',
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
                        # on_click=lambda _: page.go("/inicio"),
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
                child_aspect_ratio=1.9, # ajusta la relacion alto por ancho
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
                momentoEspecificoError = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                nombre_metodo = "pestaniaOpcion, VentanaRecambios"
                mensaje_error = f"{momentoEspecificoError} - Método: {nombre_metodo} - Error general: {e}\n"
                file.write(mensaje_error)
        finally:
            db.session.close()


    # Submenús asociados a cada opción del menú principal
    def actualizar_submenu(self, e):
        # Obtiene las opciones del submenú basadas en la selección del primer dropdown
        seleccion = e.control.value

        # Submenús asociados a cada opción del menú principal
        submenu = {
            "Aceites y liquidos": [
                "Aceite de motor",
                "Aceite de transmision y aceite de diferencial",
                "Aceite hidraulico",
                "Aceite para transmision automatica",
                "Aditivo para aceite de motor",
                "Aditivos y tratamientos para la transmision",
                "Agua destilada",
                "Anticongelante",
                "Limpiador del filtro de particulas",
                "Líquido de dirección asistida",
                "Líquido de escape diesel / adblue",
                "Líquido de frenos",
                "Líquido limpiaparabrisas",
            ],
            "Neumaticos": [
            ],
            "Frenos": [
                "Acumulador de presion del sistema de frenos",
                "Anillo de sensor de abs",
                "Bomba de vacio del sistema de frenado",
                "Boton de freno de mano",
                "Cable de freno de mano",
                "chapa protectora de disco de freno",
                "Cilindro de freno",
                "Cilindro principal de freno",
                "Deposito de liquido de frnos",
                "Discos de freno",
                "Discos y pastillas de freno",
                "Fijador de tornillos",
                "Forro de frenos alto rendimiento",
                "Freno de disco alto endimiento",
                "Freno de mano",
                "Freno de tambor",
                "Herramientas de frenos",
                "Interruptor de luz de freno",
                "Interrruptor de presion, hidraulica de freno",
                "Juego de casquillos guia, pinza de freno",
                "Kit de accesorios de las zapatas de freno",
                "Kit de accesorios de las pastillas de freno",
                "Kit de frenos de tambor",
                "Kit de reparacion de la bomba de freno",
                "Kit de reparacion de pinzas de freno",
                "Kit de reparacion del bombin de freno",
                "Kit de reparacion eje de freno de estacionamiento",
                "Latiguillos de freno",
                "Liquido de frenos",
                "Lubricantes",
                "Modulo ABS",
                "Pasta de montaje",
                "Pastillas de freno",
                "Pintura pinza de freno",
                "Pinzas de freno",
                "Piston de la pinza de freno",
                "Regulador del freno de tambor",
                "Rele de proteccion contra sobretension del ABS",
                "Repartidor de frenos",
                "Sensor ABS",
                "Sensor de aceleracion longitudinal / transversal",
                "Sensor de desgaste de pastillas de frenos",
                "Servofreno",
                "Soporte de pinzas de freno",
                "Sprays y aerosoles tecnicos",
                "Tambor de freno",
                "Tornillo del disco de freno",
                "Tuberia de freno",
                "Tubos de vacio",
                "Unidad de control del abs / asr",
                "Zapatas de freno",
                "Zapatas de freno de mano",
            ],
            "Filtros": [
                "Caja del fitro de aceite",
                "Filtro caja de cambios automatica",
                "Filtro de aceite",
                "Filtro de aire",
                "Filtro de aire de alto flujo",
                "Filtro de aire secundario",
                "Filtro de combustible",
                "Filtro de habitaculo",
                "Filtro de la bomba de cobustible",
                "Filtro deshidratador",
                "Filtro hidraulico de direccion",
                "Junta del soporte del filtro de aceite del motor",
                "Kit de cambio de aceite de caja automatica",
                "Kit de filtros",
                "Llave de filtro",
                "Soporte de la caja del filtro de aire",
                "Tubo de admision",
                "Valvula del filtro de combustible",
            ],
            "Motor": [
                "Aceite de motor",
                "Ajustador arbol de levas",
                "Amortiguador de la correa trapezoidal poli V",
                "Amortiguador hidraulico de la correa de distribucion",
                "Anticongelante",
                "Apoyo del cigüeñal",
                "Arbol de levas",
                "Arbol intermedio de compenzacion y arbol de compenzacion",
                "Balancines",
                "Biela",
                "Bobina",
                "Bomba de aceite",
                "Bomba de agua",
                "Bomba de agua + kit de correa poli V",
                "Bomba de vacio del sistema de frenado",
                "Bomba inyectora",
                "Brida de carburador",
                "Brida de refrigerante",
                "Bujias",
                "Bujias de precalentamiento",
                "Cable del acelerador",
                "Cables de bujias",
                "Cadena de accionamiento",
                "Cadena de distribucion",
                "Camisa de cilindro",
                "Carril de deslizamiento",
                "Carter de aceite",
                "Casquillo de pie de biela",
                "Casquillos de biela",
                "Caudalimetro",
                "Cigüeñal",
                "Cojinetes de arbol de levas",
                "Colector de escape",
                "Colector de admision",
                "Conector de la bujia de encendido",
                "Correa de alternador",
                "Correa de distribucion",
                "Correa tropezoidal",
                "Cuerpo de mariposa",
                "Culata"
                "Discos del cigüeñal",
                "Distribuidor",
                "Embrague viscoso de ventilador",
                "Enfriador de aceite",
                "Enfriador EGR",
                "Filtro de aceite",
                "Filtro de aire",
                "filtro de aire de alto flujo",
                "Filtro de combustible",
                "Herramientas para motor",
                "Intercooler",
                "Inyectores",
                "Juego de juntas de culata",
                "Juego de juntas de motor",
                "Junta anular, conducto de aire admision",
                "Junta de agua refrigerante",
                "Junta de bomba de aceite",
                "Junta de bomba de agua",
                "Junta de carter de distribucion",
                "Junta de colector de admision",
                "Junta de colector de escape",
                "Junta de culata",
                "Junta de enfriador de aceite",
                "Junta de inyector",
                "Junta de tapa de balancines",
                "Junta de tapon de aceite",
                "Junta de tapon de carter",
                "Junta de termostato",
                "Junta de valvula egr",
                "Junta, guia y ajuste de valvulas",
                "Junta del carter",
                "Junta del soporte del filtro de aceite del motor",
                "Junta del turbo",
                "Junta, ventilador del bloque motor",
                "Kit completo de juntas del motor",
                "Kit de cadena de distribucion",
                "Kit de correa de alternador",
                "Kit de distribucion",
                "Kit de distribucion con bomba de agua",
                "Kit de juntas de la tapa de balancines",
            ],
            "Sistema limpiaparabrisas": [
                "Bomba limpiaparabrisas",
                "Bomba lavafaros",
                "Boquilla de limpiaparabrisas",
                "Brazo de limpiaparabrisas",
                "Conector de manguito de lavado",
                "Conmutador de la columna de direccion",
                "Deposito de agua del limpiaparabrisas",
                "Escobilla limpiafaros",
                "Eyector del lavafaros",
                "Goma de limpiaparabrisas",
                "Liquido limpiaparabrisas",
                "Motor de limpiaparabrisas",
                "Rele limpiaparabrisas",
                "Sensor de lluvia",
                "Sensor, nivel agua lavado",
                "Varillaje de limpiaparabrisas",
            ],
            "Encendido y precalentamiento": [
                "Bobina",
                "Bujias",
                "Bujias de precalentamiento",
                "Cables de bujias",
                "Capsula de vacio del distribuidor de encendido",
                "Conector de la bujia de encendido",
                "Distribuidor",
                "Herramientas para encendido / precalentamiento",
                "Junta de carter de distribucion",
                "Kit de reparacion del distribuidor de encendido",
                "Modulo de encendido",
                "Rele de calentadores",
                "Rotor de distribuidor",
                "Sensor de arbol de levas",
                "Sensor de cigüeñal",
                "Sensor de detonacion",
                "Tapa antipolvo del distribuidor de encendido",
                "Tapa de delco",
                "Unidad de control, mando del motor",
            ],
            "Suspension": [
                "Anillo de sensor de abs",
                "Ballestas",
                "Barra estabilizadora",
                "Bieleta de suspension",
                "Brazo de suspension",
                "Buje de rueda",
                "Buje eje",
                "Caja cojinete rueda",
                "Caja de muelle",
                "Casquillo del pivote de la mangueta",
                "Copela de amortiguador y cojinete",
                "Eje",
                "Fuelle de direccion",
                "Guardapolvos amortiguador & topes de suspension",
                "Herramientas para suspension",
                "Kit de montaje de la barra oscilante",
                "Kit de reparacion de la barra de acoplamiento de la barra estabilizadora",
                "Kit de reparacion de la rotula de la suspension",
                "Kit de reparacion de la suspension",
                "Kit de reparacion del brazo de suspension",
                "Mangueta",
                "Pivote de direccion",
                "Reten del buje de rueda",
                "Rodamiento de rueda",
                "Rotula axial de direccion",
                "Rotula de direccion",
                "Rotula de suspension",
                "Sensor ABS",
                "Sensor de aceleracion longitudinal / transversal",
                "Sensor de presion de Neumáticos (TPMS)",
                "Sensor, luces xenon (regulacion alcance luces)",
                "Separadores de rueda",
                "Silentblock de brazo de suspension",
                "Silentblock de la barra estabilizadora",
                "Soporte de amortiguador",
                "Soporte de caja de cambios",
                "Soporte de la barra estabilizadora",
                "Soporte de motor",
                "Soporte, parachoques",
                "Suspencion de cabina",
                "Suspension de la direccion",
                "Tornillo de ajuste de la inclinacion",
                "Tornillos de rueda y tuercas de rueda",
                "Tuerca del muñon del eje",
                "Tuercas de rueda",
            ],
            "Sistema electrico": [
                "alternador",
                "Anillo de sensor de abs",
                "Antena",
                "Aparato de mando, calefaccion del asiento",
                "Bateria",
                "Bomba de limpiaparabrisas",
                "Bombilla antiniebla",
                "Bombilla de faro",
                "Bombilla de luz de freno",
                "Bombilla intermitente",
                "Bombilla para luces de marcha atras",
                "Bombillas traseras",
                "Bombin de arranque",
                "Boton de luces de emergencia",
                "Botonesra de elevalunas",
                "Cable del velocimetro",
                "Caja de fusibles",
                "Catadioptrico",
                "Caudalimetro",
                "Cierre centralizado",
                "Claxon",
                "Columna de direccion + bomba de direccion electrica",
                "Conmutador del pedal del embrague",
                "Conmutador de la columna de direccion",
                "Elevalunas",
                "Escobillas del motor de arranque",
                "Faros",
                "Faros de xenon",
                "Fusibles",
                "Herramientas para sistema electrico",
                "Iluminacion del panel de instrumentos",
                "Interruptor de espejo retrovisor",
                "Interruptor de luz de freno",
                "Interruptor de marcha atras",
                "Interruptor de puerta",
                "Junta del aforador de combustible",
                "Kit de cables",
                "Kit electrico para remolque",
                "Lampara de luz de matricula",
                "Lampara de luz habitaculo",
                "Lampara para faros de carretera",
                "Luces antiniebla",
                "Lucas de estacionamiento y luz de posicion",
                "Luces omnidireccionales",
                "Luz antiniebla trasera ",
                "Luz de maletero",
                "Luz de matricula",
                "Luz diurna (DRL)",
                "Mando de luces",
                "Motor de arranque",
                "Motor del elevalunas electrico",
                "Motor del limpiaparabrisas",
                "Motor del ventilador del radiador",
                "Motor regulador de faros",
                "Piezas de faros de luz antiniebla",
                "Piezas de luces traseras",
                "Piezas del motor de arranque",
                "Piloto intermitente",
                "Piloto trasero",
                "Polea libre del alternador",
                "Presostato aceite",
                "Presostato de aire acondicionado"
                "Recambio para faros",
            ],
            "Amortiguacion": [
                "Aceite hidraulico",
                "Amortiguadores",
                "Caja de muelle",
                "Copela de amortiguador y cojinete",
                "Guardapolvos amortiguador & topes de suspension"
                "Kit de reparacion de la suspension",
                "Kit de resortes de suspenion",
                "Kit de suspension de muelles y amortiguadores",
                "Muelles",
                "Soporte de amortiguador",
                "Soporte, parachoques",
                "Tornillo de ajuste de la inclinacion"
            ],
            "Correas, cadenas, rodillos": [
                "Bomba de agua",
                "Cadena de accionamientio",
                "Correa de alternador",
                "Correa de distribucion",
                "Herramientas para correas / cadenas",
                "Kit de correa de alternador",
                "Kit de distribucion",
                "Kit de distribucion con bomba de agua",
                "Polea de cigüeñal",
                "Polea inversion / aguia, correa de distribucion",
                "Polea inversion / guia, correa poli V",
                "Polea libre del alternador",
                "Polea tensora, correa dentada",
                "Polea tensora, correa poli V",
                "Rodilla guia / desviacion, correa trapecial",
                "Tapa de correa de distribucion",
                "Tensor de la correa de distribucion",
                "Tensor de la correa trapecial poli V",
                "Tornillo de polea",
            ],
            "Sistema de refrigeracion del motor": [
                "Anticongelante",
                "Bomba de agua",
                "Brida de refrigerante",
                "Carcasa del ventilador",
                "Enfriador de aceite",
                "Intercooler",
                "Junta de bomba de agua",
                "Junta de enfriador de aceite",
                "Junta de termostato",
                "Junta, brida agente frigorifico",
                "Kit de correa de alternador",
                "Kit de distribucion con bommba de agua",
                "Manguitos de radiador",
                "Manguito del aceite",
                "Manguito intercambiador de calor de la calefaccion",
                "Motor del ventilador del radiador",
                "Piezas de fijacion del radiador",
                "Radiador",
                "Reten del interruptor del ventilador del radiador",
                "Sellador de radiador",
                "Sensor de temperatura de aceite",
                "Sensor de temperatura del refrigerante",
                "Sensor de temperatura del ventilador del radiador",
                "Sensar del nivel de liquido refrigerante",
                "Tapa de radiador",
                "Tapon de dilatacion",
                "Tapon del radiador de refrigeracion",
                "Termostato",
                "Unidad de control del ventilador del radiador",
                "Vaso de expansion",
            ],
            "Carroceria": [
                "Aislante de capo de motor",
                "Aletines",
                "Amortiguadores de maletero",
                "Bastidor de techo",
                "Bombilla antiniebla",
                "Bombilla de faro",
                "Bombilla de luz de freno",
                "Bombilla intermitente",
                "Bombilla para luces de marcha atras",
                "Bombillas traseras",
                "Bombin de arranque",
                "Bombin de cerradura",
                "Capo",
                "Carcasa de retrovisor",
                "Cerradura",
                "Cerradura de maletero",
                "Chapa lateral",
                "Cierre centralizado",
                "Cristal de espejo retrovisor",
                "Cristal del faro antiniebla delantero",
                "Cristal faro",
                "Deposito de combustible y tapa",
                "Eje",
                "Embellecedor de parachoques",
                "Emblema",
                "Espejo retrovisor",
                "Faros",
                "Faros de carretera",
                "Guardabarros",
                "Interruptor de puerta",
                "Juego de faros principal",
                "Junta de parabrisas",
                "Lampara de luz de matricula",
                "Lampara para faros de carretera",
                "Luces antiniebla",
                "Luces de estacionamiento y luz de posicion",
                "Luneta trasera",
                "Luz de matricula",
                "Luz diurna (DRL)",
                "Manilla de puerta",
                "Moldura de paso de rueda",
                "Moldura de puerta",
                "Parabrisas",
                "parachoques",
                "Paso de rueda",
                "Piezas de faros de luz antiniebla",
                "Piezas de luces traseras",
                "Piezas de puerta",
                "Piloto intermitente",
                "Piloto trasero",
                "Protector antiempotramiento del motor",
                "Puerta trasera",
                "Recambios para faros",
                "Refuerzo parachoques",
                "Rejilla",
                "Rejilla antiniebla",
                "Revestimiento posterior",
                "Sensores de aparcamiento",
                "Soporte de parachoques",
                "Soporte de radiador",
                "Soporte para sensor de aparcamiento",
                "Spoiler delantero",
                "Sujecion del radiador",
                "Tapa de gancho remolque",
                "Tapa de motor",
                "Tercera luz de freno",
                "Umbral",
                "Ventana lateral",
            ],
            "Calefaccion y ventilacion": [
                "Filtro de habitaculo",
                "Manguito intercambiador de calor de la calefaccion",
                "Radiador de calefaccion",
                "Resistencia de ventilador de calefaccion",
                "Sensor de temperatura interior",
                "Sensor de temperatura exterior",
                "Servomotor de aire acondicionado",
                "Unidad de control de la ventilacion",
                "Ventilador de calefaccion",
            ],
            "Juntas y retenes": [
                "Juego de juntas de motor",
                "Junta de agua refrigerante",
                "Junta de bomba de agua",
                "Junta de carter de distribucion",
                "Junta de colector de admision",
                "Junta de colector de escape",
                "Junta de culata",
                "Junta de enfriador de aceite",
                "Junta de inyector",
                "Junta de parabrisas",
                "Junta tapa de balancines",
                "Junta de tapon de aceite",
                "Junta de tapon de carter",
                "Junta de termostato",
                "Junta de tubo de escape",
                "Junta de valvula egr",
                "Junta del carter",
                "Junta del turbo",
                "Junta, brida agente frigorifico",
                "Junta, carter aceite - transm. autom.",
                "Junta, ventilacion del bloque motor",
                "Juntas de bomba inyectora",
                "Kit completo de juntas del motor",
                "Kit de juntas del turbocompresor",
                "Reten de arbol de levas",
                "Reten de diferencial",
                "Reten de la bomba de aceite",
                "Reten de la transmision",
                "Reten de Palier",
                "Reten del cigüeñal",
                "Reten de valvulas",
            ],
            "Escape": [
                "Abrazadera de tubo de escape",
                "Anillo de soporte, silenciador",
                "Catalizador",
                "Cinta de goma de la linea de escape",
                "Enfriador EGR",
                "Filtro de particulas (FAP)",
                "Intercooler",
                "Juego de montaje catalizado",
                "Juego de montaje silenciador",
                "Junta de colector de escape",
                "Junta de tubo de escape",
                "Junta de valvula egr",
                "Junta del turbo",
                "Kit de sujecion del tubo de escape",
                "Modulo dosificador",
                "Pieza de fijacion para sistema de escape",
                "Sensor de presion del turbo",
                "Sensor de presion gas de escape",
                "Sensor, temp. gas escape",
                "Silenciador",
                "Soporte de tubo de escape",
                "Transductor de presion",
                "Tubo de engrase del turbo",
                "Tubo de escape",
                "Tubo flexible de escape",
                "Tubo Intercooler",
                "Turbo",
                "Valvula EGR",
            ],
            "Interior": [
                "Alfombrillas",
                "Amortiguador de maletero",
                "Antena",
                "Bombin de arranque",
                "Bombin de cerradura",
                "Boton de luces antiniebla",
                "Botonera de elevalunas",
                "Cable del velocimetro",
                "Cerradura",
                "Cierre centralizado",
                "Conmutador del pedal del embrague",
                "Conmutador en la columna de direccion",
                "Elevalunas",
                "Iluminacion del panel de instrumentos",
                "Interruptor de luz de freno",
                "Interruptor de marcha atras",
                "Interruptor de puerta",
                "Lampara de luz habitaculo",
                "Luz de maletero",
                "Luz de puerta",
                "Maletero",
                "Mando de luces",
                "Manilla de puerta",
                "Palanca de cambios",
                "Pedales y cubre pedales",
                "Rele multifuncion",
                "Resistencia de ventilador de calefaccion",
                "Revestimiento",
                "Sensor de la temperatura interior",
                "Sensor de temperatura exterior",
                "Sensor del pedal del acelerador",
                "Sensores de aparcamiento",
                "Unidad de control de la ventilacion",
            ],
            "Sistema de combustible": [
                "Arandela del inyector",
                "Bomba de combustible",
                "Bomba de combustible del interior del deposito",
                "Bomba inyectora",
                "Cable del acelerador",
                "Caja del filtro de aceite",
                "Caudalimetro",
                "Cuerpo de mariposa",
                "Deposito de combustible y tapa",
                "Filtro de combustible",
                "Herramientas para el sistema de combustible",
                "Inyectores",
                "Junta de inyector",
                "Junta del aforador de combustible",
                "Juntas de bomba inyectora",
                "Kit de reparacion de inyectores",
                "Manguitos y tuberias",
                "Rampa de inyectores",
                "Regulador de presion de combustible",
                "Sensor de la presion del combustible",
                "Sensor de nivel de combustible",
                "Sensor del pedal del accelerador",
                "Sensor tps",
                "Sistema de inyeccion",
                "Tapa de deposito de combustible",
                "Tubo de retorno de combustible",
                "Unidad de control, mando del motor",
                "Valvula de corte de combustible",
            ],
            "Direccion": [
                "Arbol de direccion",
                "Barra de acoplamiento",
                "Barra de direccion",
                "Bomba de direccion",
                "Cremallera de direccion",
                "Deposito compensacion de direccion asistida",
                "Filtro hidraulico de direccion",
                "Fuelle de direccion",
                "Kit de juntas de la bomba hidraulica",
                "Kit de reparacion, mecanismo direccion",
                "Liquido de direccion asistida",
                "Presostato aceite",
                "Rotula axial de direccion",
                "Rotula de direccion",
                "Rotula de suspension",
            ],
            "Embrague": [
                "Bomba de embrague",
                "Bombin de embrague",
                "Casquillo guia del embrague",
                "Cojinete de empuje",
                "Conmutador del pedal del embrague",
                "Disco de embrague",
                "Herramientas para embrague",
                "Horquilla de embrague",
                "Kit de embrague",
                "Kit de reparacion del cilindro receptor del embrague",
                "Limpiador de frenos",
                "Pedales y cubre pedales",
                "Plato de presion de embrague",
                "Tornillo del volante de inersia",
                "volante bimasa",
            ],
            "Palier y junta homocinetica": [
                "Cojinete intermedio del palier",
                "Fuelle palier",
                "Junta homocinetica",
                "Palier",
                "Reten de Palier",
                "Tornillos de junta homocinetica",
                "Tuercadel muñon del eje",
            ],
            "Remolque / piezas adicionales": [
                "Caballete del enganche del remolque",
                "Enganche de bola remolque",
                "Kit electrico para embrague",
                "Tapa de gancho remolque",
            ],
            "Caja de cambios": [
                "Aceite de transmision y aceite de diferencial",
                "Aceite para transmision automatica",
                "Cable de caja de cambios",
                "Cojinete de la caja de cambios",
                "Filtro caja de cambios automatica",
                "Interruptor de marcha atras",
                "Junta, carter aceite - transm. autom.",
                "Kit de cambio de aceite de caja automatica",
                "Kit reparacion de palanca de cambios",
                "Palanca de cambios",
                "Reten de la transmision",
                "Sensor de velocidad",
                "Soporte de la caja de cambios",
                "Unidad de control de la caja de cambios automatica",
                "Valvula de mando de la caja de cambios automatica",
                "Volante bimasa",
            ],
            "Aire acondicionado": [
                "Compresor de aire acondicionado",
                "Condensador de aire acondicionado",
                "Embrague del compresor del aire acondicionado",
                "Evaporador de aire acondicionado",
                "Filtro de habitaculo",
                "Filtro deshidratador",
                "Presostato de aire acondicionado",
                "Radiador de calefaccion",
                "Resistencia de ventilador de calefaccion",
                "Sensor de la temperatura interior",
                "Sensor de temperatura del ventilador del radiador",
                "Sensor de temperatura exterior",
                "Servomotor del aire acondionado",
                "Tubos de aire acondicionado",
                "Unidad de control del ventilador del radiador",
                "Valvula de compresor de aire acondicionado",
                "Valvula de expancion de aire acondicionado",
                "Ventilador de calefaccion",
            ],
            "Rodamientos": [
                "Apoyo del cigüeñal",
                "Casquillo guia del embrague",
                "Casquillos de biela",
                "Cojinete de empuje",
                "Cojinete de la caja de cambios",
                "Cojinete intermadio del palier",
                "Cojinete del arbol de levas",
                "Rodamiento de rueda",
                "Soporte de cardan",
            ],
            "Arboles de transmision y diferenciales": [
                "Aceite de transmision y aceite de diferencial",
                "Aceite para transmision automatica",
                "Reten de diferencial",
                "Soporte de cardan",
            ],
            "Sensores, reles, unidades de control": [
                "Anillo de sensor de abs",
                "Botonera de elevalunas",
                "Caudalimetro",
                "Elevalunas",
                "Interruptor de luz de frenos",
                "Interruptor de marcha atras",
                "Motor regulador de faros",
                "Presostato de aceite",
                "Presostato de aire acondicionado",
                "Regulador de presion de combustible",
                "Regulador del alternador",
                "Rele de calentadores",
                "Rele multifuncion",
                "Resistencia de ventilador de calefaccion",
                "Sensor ABS",
                "Sensor de aceleracion longitudinal / transversal",
                "Sensor de arbol de levas",
                "Sensor de cigüeñal",
                "Sensor de desgaste de pastillas de freno",
                "Sensor de la presion del combustible",
                "Sensor de la temperatura interior",
                "Sensor de nivel de combustible",
                "Sensor de presion de aceite",
                "Sensor de presion de neumaticos (TPMS)",
                "Sensor de presion del aire de admision",
                "Sensor de presion del turbo",
                "Sensor de presion gas de escape",
                "Sensor de temperatura",
                "Sensor de temperatura de aceite",
                "Sensor de temperatura del aire de admision",
                "Sensor de temperatura del refrigerante",
                "Sensor de temperatura del ventilador del radiador",
                "Sensor de temperatura exterior",
                "Sensor de velocidad",
                "Sensor del nivel del liquido refrigerante",
                "Sensor del pedal del acelerador",
                "Sensor tps",
                "Sensor, temp. gas escape",
                "Sensores de aparcamiento",
                "Soleniode de arranque",
                "Trasductor de presion",
                "Unidad de control de la caja dde cambios automatica",
                "Unidad de control de la iluminacion",
                "Unidad de control de la ventilacion",
                "Unidad de control del abs / asr",
                "Unidad de control del ventilador del radiador",
                "Unidad de control, mando del motor",
                "Valvula de compresor de aire acondicionado",
                "Valvula de control del arbol de levas",
                "Valvula de corte de combustible",
            ],
            "Accesorios para coche": [

            ],
            "Kit de reparacion": [
                "Juego de casquillos guia, pinza de freno",
                "Kit de juntas de la bomba hidraulica",
                "Kit de reparacion de inyectores",
                "Kit de reparacion de la barra de acoplamiento de la barra estabilizadora",
                "Kit de reparacion de la bomba de freno",
                "Kit de reparacion de la suspension",
                "Kit de reparacion de pinzas de freno",
                "Kit de reparacion del brazo de suspension",
                "Kit de reparacion del cilindro receptor del embrague",
                "Kit de reparacion, eje de freno de estacionamiento",
                "Kit de reparacion, mecanismo direccion ",
                "Kit reparacion de palanca de cambios",
                "Piezas del motor de arranque",
                "Repuestos de alternador",
            ],
            "Herramientas y equipo": [

            ],
            "Tuberias y mangueras": [
                "Brida de refrigerante",
                "Conector de manguito",
                "Latiguillos de freno",
                "Manguito de radiador",
                "Manguito de ventilador del carter",
                "Manguito del aceite",
                "Manguito intercambiador de calor de la calefaccion",
                "Manguito y tuberias",
                "Tuberia de freno",
                "Tubo de admision",
                "Turbo de engrase del turbo",
                "Tubo de retorno de combustible",
                "Tubo flexible, ventilador del bloque motor",
                "Tubo intercooler",
                "Tubo de aire acondicionado",
                "Tubos de vacio",
            ],
            "Productos para cuidado del coche": [

            ],
            "Iluminacion": [
                "Bombilla antiniebla",
                "Bombilla de faro",
                "Bombilla de luz de freno",
                "Bombilla intermitente",
                "Bombilla para luces de marcha atras",
                "Bombillas traseras",
                "Faros",
                "Faros auxiliares",
                "Faros de carretera",
                "Iluminacion del panel de instrumentos",
                "Lampara de luz de matricula",
                "Lampara de luz habitaculo",
                "Lampara para faros de carretera",
                "Luces antiniebla",
                "Luces de estacionamiento y luz de posicion",
                "Luz de maletero",
                "Luz de matricula",
                "Lus de puerta",
                "Luz diurna (DRL)",
                "Piloto intermitente",
                "Piloto trasero",
            ],
            "Tuning": [
                "Chiptuning",
                "Discos de freno deportivos",
                "Embrague reforzado",
                "Escape deportivo",
                "Filtro de aire de alto flujo",
                "Pastillas de freno deportivo",
                "Separadores de rueda",
                "Suspension deportiva",
            ],
            "Sujeciones": [
                "Abrazaderas",
                "Juntas toricas universales",
                "Pernos",
                "Remaches",
                "Tuercas",
            ],
        }

        # Actualizar el valor del objeto Text con la opcion elegida
        if seleccion in submenu:
            print(submenu[seleccion])
            self.submenu_opciones.options = [ft.dropdown.Option(sub) for sub in submenu[seleccion]]
            print(self.submenu_opciones.options)

        else:
            self.submenu_opciones.options = []  # Si no hay submenú, vacía las opciones
        #self.submenu_opciones.value = None  # Resetea la selección del submenú
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
        pass

    # metodo para cargar los recambios existentes en el GridView
    def buscar_recambio(self,e):
        # Limpia los controles actuales del GridView
        self.vistaResultadosBusqueda.content.controls = []

        # inputs donde el usuario ingresa el nombre, categoria y subcategoria del recambio que quiere buscar
        recambio = self.input_buscar.value.strip()  # este es el Input
        categoria = self.menu_principal.content.controls[0].value.strip()
        subcategoria = self.submenu_opciones.value.strip()

        # Buscamos el recambio por nombre (ignorando mayúsculas y minusculas)
        recambio_localizado = db.session.query(Recambio).filter(
            Recambio.nombre_recambio.ilike(f'%{recambio}%'),
            Recambio.categoria.ilike(f'%{categoria}%'),
            Recambio.subcategoria.ilike(f'%{subcategoria}%')
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
                                        ft.Text(f"{recambios.nombre_recambio}",size=10, text_align=ft.TextAlign.LEFT)
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
                                        ft.Text(f"Descripcion:", size=10, weight=ft.FontWeight.W_700,
                                                text_align=ft.TextAlign.LEFT),
                                        ft.Text(f"{recambios.descripcion}", size=10, text_align=ft.TextAlign.LEFT)
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                bgcolor="transparent",
                                padding=0,
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

    # funcion para navegar entre ventanas
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

        # Boton para activar la busqueda del ingreso y agregar nuevo nuevo ingreso
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
                        #on_click=lambda _: page.go("/inicio"),
                    ),
                    ft.IconButton(
                        content=ft.Image(src="add-new entry.png",
                                         color= "#12597b",
                                         height=30,
                                         width=30),
                        tooltip="Añadir Nuevo",
                        # on_click=lambda _: page.go("/inicio"),
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
                child_aspect_ratio=1.0,
                runs_count=2,
                spacing=1,
                run_spacing=1,
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

    # funcion para navegar entre ventanas
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
    #page.go("/inicio")
    #page.go("/clientes")
    #page.go("/vehiculos")
    page.go("/recambios")
    #page.go("/ingresos")


# instanciar y ejecutar la aplicación
ft.app(target=main, assets_dir="assets")

