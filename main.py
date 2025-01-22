from fastapi import FastAPI
import models # importamos los modelos
from database import engine
from routers import topics, auth, admin, user

if __name__ == 'main':

    app = FastAPI() # creamnos una instancia de la clase
    models.base.metadata.create_all(bind=engine) # creamos la base de datos al iniciar la aplicacion

    # importamos los routers
    app.include_router(auth.router)
    app.include_router(topics.router)
    app.include_router(user.router)
    app.include_router(admin.router)
