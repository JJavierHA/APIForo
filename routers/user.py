from fastapi import APIRouter, HTTPException, Path, Depends
from starlette import status
from models import Topic, User
from database import sesionLocal # importamos el motor de la base de datos y la sesion local
from sqlalchemy.orm import Session # importamos las seciones locales
from typing import Annotated # permite inyectar dependencias 
# importamos las clase para validar las seciones e interactuar con los topicos
from .auth import getCurrentUser
from pydantic import BaseModel
# importamos el contexto para la creacion de una contrasenia segura
from passlib.context import CryptContext

router = APIRouter(
    prefix='/user',
    tags=['User'],
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
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class ChangePassword(BaseModel):
    newPassword: str
    oldPassword: str

# funcion para visualizar los datos del usuario
@router.get("/", status_code=status.HTTP_200_OK)
async def user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authenticated fail.")
    userData = db.query(User).filter(User.id == user.get('id')).first()
    return userData

# funcion para cambiar nuemero de telefono
@router.put("changePassword", status_code=status.HTTP_204_NO_CONTENT)
async def changePassword(user: user_dependency, db: db_dependency, 
                         changePassword: ChangePassword):
    if user is None:
        raise HTTPException(status_code=401, detail="Authenticated fail.")
    userData = db.query(User).filter(User.id == user.get('id')).first()
    if not bcrypt_context.verify(changePassword.oldPassword, userData.hashedPassword):
        raise HTTPException(status_code=404, detail="Password fail.")
    userData.hashedPassword = bcrypt_context.hash(changePassword.newPassword)
    db.add(userData)
    db.commit() # guarsamos los cambios
    