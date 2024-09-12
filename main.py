from flet import *
from sqlalchemy import and_, desc, asc
from sqlalchemy.exc import SQLAlchemyError
import models
import db






if __name__ == '__main__':

    # Resetea la base de datos si existe
    # db.Base_mobile.metadata.drop_all(bind=db.engine_sqlite, checkfirst=True)

    # crea si no existen las tablas de todos los modelos que encuentre en models.py
    db.Base_mobile.metadata.create_all(db.engine_sqlite) # Base de datos Mobil

