from fastapi import APIRouter, HTTPException, Path, Depends
from starlette import status
from models import Topic
from database import sesionLocal # importamos el motor de la base de datos y la sesion local
from sqlalchemy.orm import Session # importamos las seciones locales
from typing import Annotated # permite inyectar dependencias 
from pydantic import BaseModel, Field


router = APIRouter(
    tags=['Topics']
) # creamnos una instancia de la clase

# creamos el modelo para la validacion del los campos para la consulta post
class TopicRequest(BaseModel):
    titulo: str = Field(min_length=1)
    mensaje: str = Field(min_length=3)
    fechaCreacion: int = Field(gt=1970 )
    status: bool
    autor: int = Field(gt=0)
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

#! Funciones GET
@router.get("/", status_code=status.HTTP_200_OK)
async def returnAllTopics(db: db_dependency): # inyectamos la dependencia
    return db.query(Topic).all()

@router.get("/topic/{topicId}", status_code=status.HTTP_200_OK)
async def returnOnlyTopic(db: db_dependency, topicId: int = Path(gt=0)): # validamos que los id sean mayor a 0
    topic = db.query(Topic).filter(Topic.id == topicId).first()
    if topic is not None:
        return topic
    raise HTTPException(status_code=404, detail="Topic not found.")

#! Funciones POST
@router.post("/createTopic", status_code=status.HTTP_201_CREATED)
async def createTopic(db: db_dependency, topicRequest: TopicRequest):
    topic = Topic(**topicRequest.model_dump()) # creamos un objeto de tipo topic
    db.add(topic) # lo ageragamos
    db.commit() # guardamos los cambios

#! Funcion PUT
@router.put("/updateTopic/{topicId}", status_code=status.HTTP_204_NO_CONTENT)
async def updateTopic(db: db_dependency,
                        topicRequest: TopicRequest, 
                        topicId: int = Path(gt=0)):
    topic = db.query(Topic).filter(Topic.id == topicId).first()
    if topic is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    topic.titulo = topicRequest.titulo
    topic.mensaje = topicRequest.mensaje
    topic.fechaCreacion = topicRequest.fechaCreacion
    topic.status = topicRequest.status
    topic.autor = topicRequest.autor
    topic.curso = topicRequest.curso

    db.add(topic)
    db.commit()

#! Funcion DELETED
@router.delete("/deleteTopic/{topicId}", status_code=status.HTTP_204_NO_CONTENT)
async def deleteTopic(db: db_dependency, topicId: int = Path(gt=0)):
    topic = db.query(Topic).filter(Topic.id == topicId).first()
    if topic is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.query(Topic).filter(Topic.id == topicId).delete()
    db.commit()
