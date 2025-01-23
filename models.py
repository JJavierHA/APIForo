from sqlalchemy import Column, String, Integer, Boolean, ForeignKey # importamos lo tipos de datos
from database import base # importamos el objeto de la clase declarativa

# creamos un modelo para los usuarios
class User(base):
    __tablename__ = 'users' # especificamos el nombre de la tabla
    # especificamos los datos
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, )
    hashedPassword = Column(String(200))
    nombre = Column(String(50))
    apellido = Column(String(50))
    email = Column(String(50), unique=True)
    role = Column(String(50))
    isActive = Column(Boolean, default=True)
    phone = Column(String(10))


# creamos el modelo de la base de datos
class Topic(base):
    __tablename__ = 'topics' # especificamos el nombre de la tabla
    # especificamos los datos
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(50))
    mensaje = Column(String(200))
    fechaCreacion = Column(Integer)
    status = Column(Boolean, default=False)
    curso = Column(Integer)
    owner = Column(Integer, ForeignKey("users.id"))