from sqlalchemy import Column, String, Integer, Boolean, ForeignKey # importamos lo tipos de datos
from database import base # importamos el objeto de la clase declarativa

# creamos un modelo para los usuarios
class User(base):
    __tablename__ = 'users' # especificamos el nombre de la tabla
    # especificamos los datos
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashedPassword = Column(String)
    nombre = Column(String)
    apellido = Column(String)
    email = Column(String, unique=True)
    role = Column(String)
    isActive = Column(Boolean, default=True)


# creamos el modelo de la base de datos
class Topic(base):
    __tablename__ = 'topics' # especificamos el nombre de la tabla
    # especificamos los datos
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String)
    mensaje = Column(String)
    fechaCreacion = Column(Integer)
    status = Column(Boolean, default=False)
    curso = Column(Integer)
    owner = Column(Integer, ForeignKey("users.id"))