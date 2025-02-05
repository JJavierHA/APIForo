# Foro
El proyecto es una **API REST** sencilla que efectual el funcionamiento de un foro de discusion tipico. Un foro es un espacio de reunión donde se discuten temas de interés común. Puede ser un lugar físico o virtual, y se utiliza para intercambiar opiniones, preguntas, experiencias, y habilidades. 

## Comenzando 🚀
A continuacion se declaran las instrucciones te permitiran poder replicar el proyecto en tu maquina local con la finalidad de desarrollo y pruebas.

### Pre-requisitos 📋
Nesesitas contar con las siguientes cosas para poder replicar el proyecto en tu maquina local.
* **python 3.6** (se recomienda versiones superiores o mas recientes)
* **pip** (gestor de dependencias de python)
* **Docker** o **Docker Hub** (opcional)
* **Git**

### Instalación 🔧
Clona este repositorio en tu equipo local con ayuda de git.

Efectua el siguiente comando en tu terminar en el directorio donde desees que se almacene el proyecto

**Por ssh:**
``` bash
git clone git@github.com:JJavierHA/APIForo.git
```
**O si lo prefieres por https:**
``` bash
git clone https://github.com/JJavierHA/APIForo.git
```
> [!NOTE]
> Usa python o python3 dependiendo de tu sistema operativo**

Dentro del proyecto raiz abre una terminal y crea un entorno virtual con el siguiente comando:

Activa el entorno virtual.
``` bash
python -m venv venv
```
``` bash
venv\Scripst\activate # para windows
```

``` bash
source venv/bin/activate # linux
```
Instala las dependencias del proyecto con el comando:

Esto instalara en tu entorno entorno virtual las dependencias para que el proyecto funcione correctamente.
``` bash
pip install -r requirements.txt
```

Selecciona el interprete en el ide de tu preferencia si es necesario, selecciona el correspondiente al archivo venv

## Despliegue 📦
Para el despliegue de este proyecto se requiere de docker o docker hub segun sea el caso, con la finalidad de poner en marcha los contenedores y ver el correcto funcionamiento del proyecto.

El archivo cuenta con los documentos:
* **docker-compose.yml** Para el levatamiento de la aplicacion en produccion.
* **docker-compose-dev.yml** Para el levantamiento del proyecto en desarrollo.

> [!IMPORTANT]
> * Revisa que el puerto 3306 de tu equipo no este ocupado, ya que esto puede ocacionar problemas en el deploy del proyecto.
> 
> * Configura el archivo **.env.template** de acuerdo a las instrucciones en su interior

#### Pasos para levantar la aplicacion en produccion (terminada)
``` bash
docker compose up --build # docker
```
``` bash
docker-compose up --build # docker hub
```
#### Pasos para levantar la aplicacion en desarrollo
``` bash
docker compose -f docker-compose-dev.yml up --build
```
``` bash
docker-compose -f docker-compose-dev.yml up --build
```
> [!NOTE]
> Deberas ver los logs de los contenedores en tu terminal, lo cual es señal de que todo a salido bien.

**Extra:** En una nueva terminal ejecuta el siguiente comando para ver los contenedores activos. Deberias ver los contenedores de la aplicacion en funcionamiento.
``` bash
docker ps
```
Deverias ver algo similar
| STATUS  | PORT | NAMES      |
|---------|------|----------|
| Up 46 seconds     | 0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   | apiforo-foro_api-1   |
| Up 52 seconds (healthy) | 0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   | apiforo-delfin-1   |

#### Funcionamiento:
Dirigete a tu navegador y escribe la siguiente direccion: http://localhost:8000/docs

Podras ver la documentacion auto generada por FastAPI-Swagger UI: [Auto documentacion](http://localhost:8000/docs)

![Image](https://github.com/user-attachments/assets/238bfb20-e51b-42bc-a783-00a6a2274d17)

Crea un usuario para poder hacer uso de los demas endpoints
1. Desglosa el endpoint.
2. Remplaza los datos en el json (Coloca admin en el campo role para usar las opciones de admin).
3. Ejecuta el endpoint.

![Image](https://github.com/user-attachments/assets/acd4354c-fd1f-4ef4-a7e1-b674731b996a)


Autentica el usuario
1. Presiona AUTHORIZE.
2. Ingresa tus credenciales.
3. Presiona AUTHORIZE. 

![Image](https://github.com/user-attachments/assets/ce5112fe-15b8-4881-bb55-234cb7c65aae)

![Image](https://github.com/user-attachments/assets/6bc2fbc5-e727-4c33-8ce3-9019ffac2709)

Ahora puedes usar los distindos enpoints 😉

## Construido con 🛠️

* [FastAPI](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Docker](https://maven.apache.org/) - Contenerizador de aplicaciones


## Autores ✒️

* **Jose Javier Herrera Arguello** - *Trabajo Inicial* - [JJavierHA](https://github.com/JJavierHA)
