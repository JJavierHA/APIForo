# Foro
El proyecto es una **API REST** sencilla que efectual el funcionamiento de un foro de discusion tipico. Se trata de una herramienta de gestión del tiempo que ayuda a organizar el trabajo o la vida personal. Un foro es un espacio de reunión donde se discuten temas de interés común. Puede ser un lugar físico o virtual, y se utiliza para intercambiar opiniones, preguntas, experiencias, y habilidades. 

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
> **Nota: Usa python o python3 dependiendo de tu sistema operativo**

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
Instalas las dependencias del proyecto con el comando:
Esto instalara en tu entorno entorno virtual las dependencias para que el proyecto funcione correctamente.
``` bash
pip install -r requirements.txt
```
 **Importante:**
Configura el archivo **.env.template** de acuerdo a las instrucciones en su interior

## Despliegue 📦
Para el despliegue de este proyecto se requiere de docker o docker hub segun sea el caso, con la finalidad de poner en marcha los contenedores y ver el correcto funcionamiento del proyecto.

El archivo cuenta con los documentos:
* **docker-compose.yml** Para el levnatamiento de la aplicacion en produccion.
* **docker-compose-dev.yml** Para el levantamiento del proyecto en desarrollo.

#### Pasos para levantar la aplicacion en produccion (terminada)
``` bash
docker compose up --build
```
#### Pasos para levantar la aplicacion en desarrollo
``` bash
docker compose -f docker-compose-dev.yml up --build
```
Nota: deberas ver los logs de los contenedores en tu terminal, lo cual es senial de que todo a salido bien.
**Extra:** 
Ejecuta el siguiente comando para ver los contenedores activos. Deberias ver los contenedores de la aplicacion en funcionamiento
``` bash
docker ps
```
Deverias ver algo similar
| STATUS  | PORT | NAMES      |
|---------|------|----------|
| Up 46 seconds     | 0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   | apiforo-foro_api-1   |
| Up 52 seconds (healthy) | 0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   | apiforo-delfin-1   |

#### Funcionamiento:
Dirigete a tu navegador y escribe la siguiente direccion:
FastAPI-Swagger UI: [Auto documentacion](http://localhost:8000/docs)
Podras ver la documentacion auto generada por fastAPI

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS


## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Andrés Villanueva** - *Trabajo Inicial* - [villanuevand](https://github.com/villanuevand)
* **Fulanito Detal** - *Documentación* - [fulanitodetal](#fulanito-de-tal)
