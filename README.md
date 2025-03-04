# SaludTech Alpes - Medical History Service
Este repositorio contiene el servicio de historial medico para el proyecto **SaludTech Alpes**. Este servicio implementa una arquitectura basada en **eventos y comandos**, utilizando **CQRS** y separación de responsabilidades para garantizar modularidad y escalabilidad.

![Github](https://github.com/SaludTechAlpes/saludtechalpes-medical-history-service/actions/workflows/action.yaml/badge.svg)
![Github](https://github.com/SaludTechAlpes/saludtechalpes-medical-history-service/actions/workflows/merge-to-develop.yaml/badge.svg)
![Github](https://github.com/SaludTechAlpes/saludtechalpes-medical-history-service/actions/workflows/release-to-main.yaml/badge.svg)

## 📂 Estructura del Proyecto

El proyecto sigue una estructura modular organizada por capas de **Dominio, Aplicación e Infraestructura**, siguiendo los principios de **Domain-Driven Design (DDD)**. A continuación, se describe cada parte:

### **1.** **`src/config`**

Contiene la configuración del proyecto:

- `config.py`: Configuraciones generales de la aplicación.
- `db.py`: Configuración de la base de datos y conexión.

### **2.** **`src/modulos`**

Aquí se encuentran los módulos principales del sistema.

#### **2.1 `historialMedico`**

Este módulo se encarga de recibir eventos de información de los data frames para extraer la data del paciente y almacenarlos en la base de datos

- **`aplicacion`**: Contiene la lógica de aplicación y los servicios encargados de coordinar procesos de negocio.
- **`dominio`**: Define las entidades, reglas de negocio, eventos de dominio y puertos.
- **`infraestructura`**: Implementaciones concretas de los puertos, repositorios, adaptadores y consumidores de eventos.
- **`eventos.py`**: Define los eventos de dominio relacionados con la anonimización de datos.
- **`comandos.py`**: Define los comandos ejecutados dentro del proceso de anonimización.

### **3. `src/seedwork`**

Este módulo contiene código reutilizable para todas las aplicaciones dentro del sistema.

- **`aplicacion`**: Define servicios genéricos, comandos y handlers.
- **`dominio`**: Contiene las abstracciones de entidades, eventos, objetos de valor, reglas de negocio y repositorios.
- **`infraestructura`**: Define implementaciones genéricas de consumidores de eventos, repositorios y en general puertos.

## 🔄 **Flujo de Trabajo del Sistema**

El sistema sigue un flujo basado en **eventos y comandos**:

1. **Consumo evento dataframe**: El servicio data transformation, envia evento con datos de dataframe con la ruta de acceso para obtener metadatos del paciente.
2. **Se consulta la ruta**: Se ejecuta capa de aplicación y se obtienen extraen los datos del paciente y se almacenan en la base de datos

## 🚀 **Cómo Ejecutar la Aplicación**

### **1. Configuración previa (si no se usa Gitpod)**

Si no estás utilizando Gitpod, es necesario ejecutar los siguientes comandos antes de iniciar la aplicación para el correcto funcionamiento de Pulsar:

```bash
mkdir -p data/bookkeeper && mkdir -p data/zookeeper && sudo chmod -R 777 ./data
```

### **2. Desplegar con Docker Compose**

```bash
make docker-up
```
O si no tiene instalado make

```bash
docker-compose up --build
```

### **3. En caso de errores con Bookkeeper o Zookeeper**

Si los contenedores de **Bookkeeper** o **Zookeeper** fallan o se reinician constantemente, sigue estos pasos:

```bash
docker-compose down -v
rm -rf data
mkdir -p data/bookkeeper && mkdir -p data/zookeeper && sudo chmod -R 777 ./data
make docker-up
```

## 🛠 **Endpoints de la API**

### **1. Verificar estado del servicio**

**Endpoint:** `GET /health`

**Descripción:** Retorna el estado de la aplicación.

**Ejemplo de solicitud con curl:**

```bash
curl -X GET http://localhost:5000/health
```

**Respuesta:**

```json
{
  "status": "up",
  "application_name": "SaludTech Alpes",
  "environment": "development"
}
```

# Description
This is a python 🐍 flask 🌶️ service to record the medical history 🩺📋

# Made with
[![Python](https://img.shields.io/badge/python-2b5b84?style=for-the-badge&logo=python&logoColor=white&labelColor=000000)]()
[![Flask](https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white&labelColor=000000)]()

# How to execute

If you want execute without docker then you can use the next commands in your terminal.
Note: firstable is important that you have your python virtual environmente created.

into directory flaskr execute
```bash
$ flask --app ./src run
```

# Prerequirements


* Python 🐍
* Docker & docker-compose 🐳 (Optional).
* For Linux 🐧 and mac 🍎 you can use makefile.
* For Windows 🪟 you can use bash function.

# How to execute with docker 🐳

1. Step one locate in the root of the project

```bash
$ cd saludtechalpes-medical-history-service
```

2. Run in docker 🐳

```bash
# With Linux 🐧 or Mac 🍎
$ make docker-local-up

# With Windows 🪟
$ source run.sh; docker_local_up

# With docker compose for all Operative Systems

$ docker compose -f=docker-compose.local.yaml up --build
```

3. Make sure that all microservices are running

* Executing this command

```bash
$ docker ps
```
<img width="1389" alt="Screenshot 2025-02-28 at 11 04 05 PM" src="https://github.com/user-attachments/assets/25f7c8aa-a53b-4d5d-b54b-f3087777f96f" />

4. Execute the **health** api rest with cUrl or you could use postman 👩🏻‍🚀 in order to validate the health 💚

```bash
curl --location 'http://localhost:3002/health' --header 'Content-Type: application/json'
```

### Body in JSON

```json
{
    "application_name": "saludtechalpes-medical-history-service",
    "environment": "local",
    "status": "up"
}

```

5. Finally, shutdown the environment in docker 🐳
```bash
# With Linux 🐧 or Mac 🍎
$ make docker-dev-down

# With Windows 🪟
$ source run.sh; docker_local_down

# With docker compose for all Operative Systems

$ docker compose -f=docker-compose.local.yaml down
```
