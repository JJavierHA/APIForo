from fastapi import FastAPI
import models # importamos los modelos
from database import engine
from routers import topics

if __name__ == 'main':

    app = FastAPI() # creamnos una instancia de la clase
    models.base.metadata.create_all(bind=engine) # creamos la base de datos al iniciar la aplicacion
    app.include_router(topics.router)# importamos los routers