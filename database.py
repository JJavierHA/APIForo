from sqlalchemy import create_engine # importamos el motor de la base de datos
from sqlalchemy.orm import sessionmaker # importamos el modulo para el uso de sesiones locales
from sqlalchemy.ext.declarative import declarative_base # importamos el modulo para interactura con la base de datos


SQLALCHEMY_DATABASE_URL = "sqlite:///./Foro.db" # creamos la ruta donde se creara la base de datos

# creamos el motor para interactura con la base de datos
# ajustamos para poder usar multi hilos
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# configuramos la sesion local a la cual le pasamos el motor para interactuar con la BD
# desactivamos el auto-commit y el auto-flush
sesionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base() # creamos una instancia de declarative base para realizar opraciones dentro de la BD
