from fastapi import APIRouter, Depends, HTTPException
from models import User # importamos el modelo de usuario
from database import sesionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic import BaseModel
from starlette import status
# importamos el contexto para la creacion de una contrasenia segura
from passlib.context import CryptContext
# importamos los modulos para la seguridad
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer # creara un formulario automatico que sera mas seguro
# importamos lo relacionado al token JWT
from datetime import timedelta, datetime, timezone
from jose import jwt, JWTError

router = APIRouter(
    tags=['Auth']
)

# pasamos los datos necesarios para crear un token jwt
SECRET_KEY = '20ef91141679795693481fb6d49b0dc6' # llave de seguridad
ALGORIMTH = "HS256" # algoritmo de encriptamiento

# creamos la funcio de dependencia
def get_db():
    db = sesionLocal()
    try:
        yield db
    finally:
        db.close()

# creamos la inyeccion de dependencias
db_dependency = Annotated[Session, Depends(get_db)]

# creamos el contexto de la contrasenia segura
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto') # agregamos el contexto de encriptado el esquema que usara

oauth2Bearer = OAuth2PasswordBearer(tokenUrl='token')

# creamos la clase validadora
class UserRequest(BaseModel):
    username: str
    password: str
    nombre: str
    apellido: str
    email: str
    role: str

# establecemos el modelo que sera base para la devolucion de servidor
class Token(BaseModel):
    access_token: str
    token_type: str

def authenticateUser(username: str, password: str, db):
    user = db.query(User).filter(User.username==username).first() # estraemos el usuario si hay coincidencias
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashedPassword):
        return False
    return user

# creamos una funcion para crear un token jwt
def createAccessToken(username: str, userId: int, role:str, expiresDelta: timedelta):
    # asignamos los datos a convertir en el payload (carga util)
    encode = {"sub": username, "id": userId, "role":role}
    # establecemos el tiempo de vida del token comenzando desde la hora actual y sumandole el tiempo de vida que ahora este posee
    expires = datetime.now(timezone.utc) + expiresDelta
    encode.update({"exp": expires})
    # * especificamos los elementos del jwt
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORIMTH) # codificamos el token con su {header:payload:firmaDigital}

#* creamos una funcion para validar si el jwt es valido 
async def getCurrentUser(token: Annotated[str, Depends(oauth2Bearer)]): # resivira un dato de tipo token
    # trataremos de obtener un payload valido
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORIMTH)
        username: str = payload.get('sub')
        idUser: str = payload.get('id')
        role: str = payload.get('role')
        # validamos si existe
        if username is None or idUser is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                detail="User not authenticated.")
        return {"username": username, "id": idUser, "role":role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                detail="User not authnticated.")


# creamo un endpoint para crear usuarios
@router.post("/auth", status_code=status.HTTP_201_CREATED)
async def createUser(db: db_dependency, userRequest: UserRequest):
    user = User(
        username=userRequest.username,
        hashedPassword=bcrypt_context.hash(userRequest.password), # creamos un has de la contrasenia para almacenarla
        nombre=userRequest.nombre,
        apellido=userRequest.apellido,
        email=userRequest.email,
        role=userRequest.role
    )
    db.add(user)
    db.commit()

# creamos una funcion que devolvera un token si el usuario esta autenticado dentro de la db
@router.post("/token", response_model=Token)
async def loginForAccessToken(dataForm: Annotated[OAuth2PasswordRequestForm, Depends()], 
                              db: db_dependency):
    # autenticamos al usuario
    user = authenticateUser(dataForm.username, dataForm.password, db)
    if not user:
        raise HTTPException(status_code=401, detail="User not autenticated.")
    token = createAccessToken(user.username, user.id, user.role, timedelta(minutes=20)) # creamos un token
    return {"access_token": token, "token_type": "bearer"} # seguimos la estructura del modelo de respuesta