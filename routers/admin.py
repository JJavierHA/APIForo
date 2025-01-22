from fastapi import APIRouter, HTTPException, Path, Depends
from starlette import status
from models import Topic
from database import sesionLocal # importamos el motor de la base de datos y la sesion local
from sqlalchemy.orm import Session # importamos las seciones locales
from typing import Annotated # permite inyectar dependencias 
# importamos las clase para validar las seciones e interactuar con los topicos
from .auth import getCurrentUser


router = APIRouter(
    prefix='/admin',
    tags=['Admin'],
) # creamnos una instancia de la clase


# creamos la dependencia para la sesion de la base de datos
def get_db():
    db = sesionLocal() # creamos una instancia de la secion local
    try:
        yield db # lanzamos db para ser usado por el contexto
    finally:
        db.close() # cerramos la conexion

# creamo la inyeccion de dependencias
db_dependency = Annotated[Session, Depends(get_db)] # tipo de dato, funcion de la que depende 
user_dependency = Annotated[dict, Depends(getCurrentUser)] # creamos una dependecia que validara las sesiones de lo susuarios

# funcion para obtener todos los topicos solo si es admin
@router.get('/topics', status_code=status.HTTP_200_OK)
async def getAllTopics(user: user_dependency, db: db_dependency):
    if user is None or user.get('role') != 'admin':
        raise HTTPException(status_code=401, detail="Authenticated fail.")
    return db.query(Topic).all()

# funcion que retorna un todo especifico solo si es admin
@router.get('/topics/{topicId}', status_code=status.HTTP_200_OK)
async def getTopibyId(user: user_dependency, db: db_dependency, 
                      topicId: int = Path(gt=0)):
    if user is None or user.get('role') != 'admin':
        raise HTTPException(status_code=401, detail="Authenticated fail.")
    topic = db.query(Topic).filter(Topic.id == topicId).first()
    if topic is None:
        raise HTTPException(status_code=404, detail="Topic not found.")
    return topic

# agregamos una funcion post para eliminar un todo especifico 
@router.delete("/deleteTopic/{topicId}", status_code=status.HTTP_204_NO_CONTENT)
async def deletTopic(user: user_dependency, db: db_dependency, 
                     topicId: int = Path(gt=0)):
    if user is None or user.get('role') != 'admin':
        raise HTTPException(status_code=401, detail="Authenticated fail.")
    topic = db.query(Topic).filter(Topic.id == topicId).first()
    if topic is None:
        raise HTTPException(status_code=404, detail="Topic not found.")
    db.query(Topic).filter(Topic.id == topicId).delete()
    db.commit() # guardamos los cambios manualmente