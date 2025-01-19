from fastapi import APIRouter, HTTPException, Path, Depends
from starlette import status
from models import Topic
from database import sesionLocal # importamos el motor de la base de datos y la sesion local
from sqlalchemy.orm import Session # importamos las seciones locales
from typing import Annotated # permite inyectar dependencias 
from pydantic import BaseModel, Field
# importamos las clase para validar las seciones e interactuar con los topicos
from .auth import getCurrentUser


router = APIRouter(
    tags=['Topics']
) # creamnos una instancia de la clase

# creamos el modelo para la validacion del los campos para la consulta post
class TopicRequest(BaseModel):
    titulo: str = Field(min_length=1)
    mensaje: str = Field(min_length=3)
    fechaCreacion: int = Field(gt=1970 )
    status: bool
    curso: int = Field(gt=0)

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

#! Funciones GET
@router.get("/", status_code=status.HTTP_200_OK)
async def returnAllTopics(user: user_dependency, db: db_dependency): # inyectamos la dependencia
    if user is None:
        raise HTTPException(status_code=401, detail="Authenticated fail.")
    return db.query(Topic).filter(Topic.owner == user.get("id")).all()

@router.get("/topic/{topicId}", status_code=status.HTTP_200_OK)
async def returnOnlyTopic(user: user_dependency, db: db_dependency, topicId: int = Path(gt=0)): # validamos que los id sean mayor a 0
    if user is None:
        raise HTTPException(status_code=401, detail="Authenticated fail.")
    topic = db.query(Topic).filter(Topic.id == topicId)\
        .filter(Topic.owner == user.get('id')).first()
    if topic is not None:
        return topic
    raise HTTPException(status_code=404, detail="Topic not found.")

#! Funciones POST
@router.post("/createTopic", status_code=status.HTTP_201_CREATED)
async def createTopic(user: user_dependency, db: db_dependency, 
                      topicRequest: TopicRequest):
    if user is None:
        raise HTTPException(status_code=401, detail="Authenticated fail.")
    topic = Topic(**topicRequest.model_dump(), owner=user.get('id') ) # creamos un objeto de tipo topic
    db.add(topic) # lo ageragamos
    db.commit() # guardamos los cambios

#! Funcion PUT
@router.put("/updateTopic/{topicId}", status_code=status.HTTP_204_NO_CONTENT)
async def updateTopic(user: user_dependency, db: db_dependency, 
                      topicRequest: TopicRequest, topicId: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail="Authenticated fail.")
    topic = db.query(Topic).filter(Topic.id == topicId)\
        .filter(Topic.owner == user.get('id')).first()
    if topic is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    topic.titulo = topicRequest.titulo
    topic.mensaje = topicRequest.mensaje
    topic.fechaCreacion = topicRequest.fechaCreacion
    topic.status = topicRequest.status
    topic.curso = topicRequest.curso

    db.add(topic)
    db.commit()

#! Funcion DELETED
@router.delete("/deleteTopic/{topicId}", status_code=status.HTTP_204_NO_CONTENT)
async def deleteTopic(user: user_dependency, db: db_dependency, topicId: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=401, detail="Authenticated fail.")
    topic = db.query(Topic).filter(Topic.id == topicId)\
        .filter(Topic.owner == user.get('id')).first()
    if topic is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.query(Topic).filter(Topic.id == topicId)\
        .filter(Topic.owner == user.get('id')).delete()
    db.commit()
