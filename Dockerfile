# Establecemos la imagen que sera usada para la constuccion del contenedor
FROM python:3.12

# establecemos la ruta sobre la cual
WORKDIR /home/app/

# copiamos las dependencias y el directorio base de nuestro proyecto
COPY ./ ./

COPY requirements.txt ./

# instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# exponemos el puerto que sera visible pos la aplicacion
EXPOSE 8000

# ejecutamos los comandos para iniciar el contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# construimos la imagen con 
# docker build -t <Nombre-Imagen>:<tag> <directorio(por defecto "." -> ruta actual)>


