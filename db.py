# Gracias a estas líneas de código, enfrento el mundo cada día 💪
# Aqui va la configuracion de la base de datos

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

'''El engine permite a SQLAlchemy comunicarse con la base de datos en un dialogo concreto
   https://docs.sqlalchemy.org/en/14/core/engines.html'''

engine_sqlite = create_engine('sqlite:///database/mobile.db',
                              connect_args={"check_same_thread": False})

'''Advertencia: crear el engine no conecta inmediatamente con la DB, eso lo hacemos despues
   Creamos la session, lo que permite realizar transacciones (operaciones) dentro de nuestra DB'''

# Crear una nueva sesión para la base de datos de el mobil
Session = sessionmaker(bind=engine_sqlite)
session = Session()

'''Ahora vamos al fichero models.py en los modelos (clases) donde queremos
   que se transformen en tablas, le añadiremos esta variable y esto se encargara de mapear
   y vincular cada clase a cada tabla'''

#Base = declarative_base()  # Esto mapeará nuestras clases de modelo a las tablas en la base de datos.
Base_mobile = declarative_base() # Esto mapeará nuestras clases de modelo a las tablas en la base de datos.
