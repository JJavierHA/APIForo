from sqlalchemy import Column, String, Integer, Boolean # importamos lo tipos de datos
from database import base # importamos el objeto de la clase declarativa

# creamos el modelo de la base de datos
class Topic(base):
    __tablename__ = 'topics' # especificamos el nombre de la tabla
    # especificamos los datos
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String)
    mensaje = Column(String)
    fechaCreacion = Column(Integer)
    status = Column(Boolean, default=False)
    autor = Column(Integer)
    curso = Column(Integer)